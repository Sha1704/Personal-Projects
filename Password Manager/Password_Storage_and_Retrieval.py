from Security_and_Encryption import Security_and_Encryption as SEC
import backend_sql as sql
from dotenv import load_dotenv
import os
import base64

load_dotenv()

database_host = os.getenv("DB_HOST")
database_user = os.getenv("DB_USER")
database_password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

# sec_class = SEC()
sql_class = sql.Backend(database_host, database_user, database_password, database)

class StorageAndRetrieval:

    def addPassword(self, key, accountName, personal_username, account_username, password, url = '', notes = ''):

        sec_class = SEC(key = key)

        encrypted_password = sec_class.encryptData(password)
        nonce = base64.b64encode(encrypted_password[0])
        cipher = base64.b64encode(encrypted_password[1])
        tag = base64.b64encode(encrypted_password[2])

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
    
        query = 'select encrypted_account_password, Nonce, Tag from account_password where lower(account_name) = %s and username = %s;'

        result = sql_class.run_query(query, (accountName.lower(),userName.lower()))
        
        if result:
            cipher = base64.b64decode(result[0][0])
            nonce = base64.b64decode(result[0][1])
            tag = base64.b64decode(result[0][2])
            sec_class = SEC(key=key)
            decrypted_password = sec_class.decryptData(nonce, cipher, tag, key)
            return decrypted_password
        else:
            return None
    
    def getAllPasswords(self, username, master_password, key):

        sec_class = SEC(key = key)

        # use query to search for master password hash
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
                    print(f'Account Name: {account_name} -- Password: {plain_pw}')
            else:
                print('Master password incorrect')
        else:
            print('Username not found')

    def updatePassword(self, username, accountName, newPassword, key):

        sec_class = SEC(key = key)
        
        new_encrypted_password = sec_class.encryptData(newPassword)
        nonce = new_encrypted_password[0]
        cipher = new_encrypted_password[1]
        tag = new_encrypted_password[2]

        replacement_query = 'UPDATE account_password SET encrypted_account_password = %s, Nonce = %s, Tag = %s WHERE username = %s AND account_Name = %s;'
        updated = sql_class.run_query(replacement_query, (cipher, nonce, tag, username.lower(), accountName.lower()))

        if updated:
            return True
        else:
            return False
    
    def removeAccount(self, accountName, username):
       
        query = "DELETE FROM account_password WHERE account_name = %s and username = %s;"
        deleted = sql_class.run_query(query, (accountName.lower(),username.lower()))

        if deleted:
            return True
        else:
            return False
