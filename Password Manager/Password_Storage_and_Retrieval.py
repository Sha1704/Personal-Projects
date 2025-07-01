from Security_and_Encryption import Security_and_Encryption as SEC
import backend_sql as sql

sql_class = sql.Backend('localhost', 'root', 'SQLinjection1.', 'password_manager')

class StorageAndRetrieval:

    def addPassword(self, accountName, personal_username, account_username, password, url = '', notes = ''):

        encrypted_password = SEC.encryptData(password)
        nonce = encrypted_password[0]
        cipher = encrypted_password[1]
        tag = encrypted_password[2]

        query = 'INSERT INTO account_password (account_name, username, account_username, encrypted_account_password, url, notes, Nonce, Tag) VALUES (%s, %s, %s,%s, %s, %s,%s, %s);'
        inserted = sql_class.run_query(query, (accountName, personal_username, account_username, cipher, url, notes, nonce, tag))

        if inserted:
            return True
        else:
            return False

    def getPassword(self, accountName):
    
        query = 'select encrypted_account_password from account_password where lower(account_name) = %s;'

        result = sql_class.run_query(query, (accountName,))
        
        if result:
            encrypted_password = result[0][0]
            decrypted_password = SEC.decryptData(encrypted_password)
            return decrypted_password
        else:
            return None
    
    def getAllPasswords(self, username, master_password):

        master_password_hash = SEC.hash_password(master_password)
        # use query to search for master password hash
        query = "select master_password_hash from user where master_password_hash = %s;"
        database_hash = sql_class.run_query(query, (master_password_hash,))

        if database_hash and master_password_hash == database_hash[0][0]:
            query2 = "select account_name, encrypted_account_password from account_password where LOWER(username) = %s;"
            encrypted_acc_password = sql_class.run_query(query2, (username.lower(),))
            for account_name, encrypted_pw in encrypted_acc_password:
                plain_pw = SEC.decryptData(encrypted_pw)
                print(f'Account Name: {account_name} Password: {plain_pw}')
        else:
            print('master password or username not found')

    def updatePassword(self, username, accountName, newPassword):
        
        new_encrypted_password = SEC.encryptData(newPassword)
        nonce = new_encrypted_password[0]
        cipher = new_encrypted_password[1]
        tag = new_encrypted_password[2]

        replacement_query = 'UPDATE account_password SET encrypted_account_password = %s, Nonce = %s, Tag = %s WHERE username = %s AND accountName = %s;'
        updated = sql_class.run_query(replacement_query, (cipher, nonce, tag, username, accountName))

        if updated:
            return True
        else:
            return False
    
    def removeAccount(self, accountName, username):
       
        query = "DELETE FROM account_password WHERE LOWER(account_name) = %s and LOWER(username) = %s;"
        deleted = sql_class.run_query(query, (accountName.lower(),username.lower()))

        if deleted:
            return True
        else:
            return False
