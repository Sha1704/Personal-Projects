from Security_and_Encryption import Security_and_Encryption as SEC
import backend_sql as sql
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

database_host = os.getenv("DB_HOST")
database_user = os.getenv("DB_USER")
database_password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

# Create database handler
sql_class = sql.Backend(database_host, database_user, database_password, database)

class StorageAndRetrieval:
    """
    Handles storing, retrieving, updating, and deleting account passwords.
    """

    def addPassword(self, key, accountName, personal_username, account_username, password, url = '', notes = ''):
        """
        Encrypts and stores a password for an account.

        :param key: Encryption key
        :param accountName: Name of the account
        :param personal_username: Username in password manager
        :param account_username: Username/email for the account
        :param password: Password to store
        :param url: Optional URL for the account
        :param notes: Optional notes
        :return: True if added, False otherwise
        """
        sec_class = SEC(key = key)

        encrypted_password = sec_class.encryptData(password)
        nonce = encrypted_password[0].decode('utf-8')
        cipher = encrypted_password[1].decode('utf-8')
        tag = encrypted_password[2].decode('utf-8')

        query = '''
           INSERT INTO account_password (account_name, username, account_username, encrypted_account_password, url, notes, Nonce, Tag) 
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        inserted = sql_class.run_query(query, (accountName.lower(), personal_username.lower(), account_username.lower(), cipher, url.lower(), notes.lower(), nonce, tag))

        if inserted:
            return True
        else:
            return False

    def getPassword(self, accountName,userName, key):
        """
        Retrieves and decrypts a password for a specific account.

        :param accountName: Name of the account
        :param userName: Username in password manager
        :param key: Encryption key
        :return: Decrypted password or None
        """
        query = 'select encrypted_account_password, Nonce, Tag from account_password where lower(account_name) = %s and username = %s;'

        result = sql_class.run_query(query, (accountName.lower(),userName.lower()))
        
        if result:
            cipher = result[0][0].strip()
            nonce = result[0][1].strip()
            tag = result[0][2].strip()
            sec_class = SEC(key=key)
            decrypted_password = sec_class.decryptData(nonce, cipher, tag, key)
            return decrypted_password
        else:
            return None
    
    def getAllPasswords(self, username, master_password, key):
        """
        Retrieves and prints all passwords for a user after verifying master password.

        :param username: Username in password manager
        :param master_password: Master password for verification
        :param key: Encryption key
        """
        sec_class = SEC(key = key)

        # Verify master password
        query = "select master_password_hash from user where username = %s;"
        database_hash = sql_class.run_query(query, (username.lower(),))

        if database_hash:
            password_hash = database_hash[0][0]
            verified = sec_class.verify_hashed_password(master_password, password_hash)

            if verified:
                query2 = "select account_name, encrypted_account_password, Nonce, Tag from account_password where LOWER(username) = %s "
                encrypted_acc_password = sql_class.run_query(query2, (username.lower(),))
                for account_name, encrypted_pw, nonce, tag in encrypted_acc_password:
                    plain_pw = sec_class.decryptData(nonce, encrypted_pw, tag, key)
                    print(f'Account Name: {account_name} \t \t Password: {plain_pw}')
            else:
                print('Master password incorrect')
        else:
            print('Username not found')

    def updatePassword(self, username, accountName, newPassword, key):
        """
        Updates the password for a specific account.

        :param username: Username in password manager
        :param accountName: Account name to update
        :param newPassword: New password to store
        :param key: Encryption key
        :return: True if updated, False otherwise
        """
        sec_class = SEC(key = key)
        
        nonce_b64, cipher_b64, tag_b64 = sec_class.encryptData(newPassword)
        nonce_str = nonce_b64.decode('utf-8')
        cipher_str = cipher_b64.decode('utf-8')
        tag_str = tag_b64.decode('utf-8')

        replacement_query = 'UPDATE account_password SET encrypted_account_password = %s, Nonce = %s, Tag = %s WHERE username = %s AND account_Name = %s;'
        updated = sql_class.run_query(replacement_query, (cipher_str, nonce_str, tag_str, username.lower(), accountName.lower()))

        if updated:
            return True
        else:
            return False
    
    def removeAccount(self, accountName, username):
        """
        Removes an account and its password from the password manager.

        :param accountName: Name of the account to remove
        :param username: Username in password manager
        :return: True if deleted, False otherwise
        """
        query = "DELETE FROM account_password WHERE account_name = %s and username = %s;"
        deleted = sql_class.run_query(query, (accountName.lower(),username.lower()))

        if deleted:
            return True
        else:
            return False
