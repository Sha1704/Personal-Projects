import backend_sql as sql
import random
import Security_and_Encryption as sec
from dotenv import load_dotenv
import os
import base64
from secrets import token_bytes

# Load environment variables from .env file
load_dotenv()

database_host = os.getenv("DB_HOST")
database_user = os.getenv("DB_USER")
database_password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

# Create backend database handler
backend = sql.Backend(database_host, database_user, database_password, database)

class UserManagement:
    """
    Handles user account management: creation, login, password changes, and deletion.
    """

    def create_user(self, username, masterPassword, email):
        """
        Creates a new user account with a unique username and stores hashed password.

        :param username: Desired username
        :param masterPassword: User's master password
        :param email: User's email address
        :return: True if user created, False otherwise
        """
        try:
            # Check if email already exists
            email_query = 'SELECT user_email FROM user WHERE user_email = %s'
            email_exists = backend.run_query(email_query, (email,))

            if email_exists:
                print('The email you entered is already in use')
                return False
            else:
                # Generate unique username with random tag
                random_tag = random.randint(0,5000)
                new_username = username + '#' + str(random_tag)

                # Try to ensure username is unique
                for _ in range(1000): 
                    random_tag = random.randint(0, 5000)
                    new_username = username + '#' + str(random_tag)
                    username_query = 'select * from user where username = %s;'
                    query_result = backend.run_query(username_query, (new_username,))
                    if not query_result:
                        break
                    else:
                        raise Exception("Failed to generate a unique username")
                
                print(f'Your new username is {new_username}. Please keep track of this username as you\'ll use this to sign in from now on')
                        
                # Prepare to insert new user
                query = 'INSERT INTO user (username, master_password_hash, encryption_key, user_email) VALUES (%s, %s, %s, %s);'

                key = self.create_key()
                security = sec.Security_and_Encryption(key=key)
                hashed_password = security.hash_password(masterPassword)
                encoded_key = base64.b64encode(key)

                backend.run_query(query, (new_username.lower(), hashed_password, encoded_key, email.lower()))

                return True
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def log_in(self, username, masterPassword):
        """
        Authenticates a user by verifying the master password.

        :param username: Username to log in
        :param masterPassword: Master password to verify
        :return: Tuple (True, encryption_key) if successful, (False, None) otherwise
        """
        try:
            username_query = 'SELECT master_password_hash FROM user WHERE username = %s;'
            encryption_key_query = 'SELECT encryption_key FROM user WHERE username = %s;'

            result = backend.run_query(username_query, (username.lower(),))
            key_result = backend.run_query(encryption_key_query, (username.lower(),))
            if result and key_result:
                stored_password_hash = result[0][0]
                encrypted_key_b64 = key_result[0][0]
                encryption_key = base64.b64decode(encrypted_key_b64)
                security = sec.Security_and_Encryption(key = encryption_key)
                if security.verify_hashed_password(masterPassword, stored_password_hash):
                    print('Login successful!')
                    return True, encryption_key
                else:
                    print('Username or password incorrect')
                    return False, None
        except Exception as e:
            print(f"An error occurred: {e}")
            return False, None

    def changeMasterPassword(self, username, oldPassword, newPassword):
        """
        Changes the user's master password after verifying the old password.

        :param username: Username whose password is to be changed
        :param oldPassword: Current master password
        :param newPassword: New master password
        :return: True if password changed, False otherwise
        """
        try:
            query = 'SELECT master_password_hash, encryption_key FROM user WHERE username = %s;'
            result = backend.run_query(query, (username.lower(),))
            if result:
                stored_hash = result[0][0]
                encrypted_key_b64 = result[0][1]
                encryption_key = base64.b64decode(encrypted_key_b64)
                security = sec.Security_and_Encryption(key=encryption_key)
                if security.verify_hashed_password(oldPassword, stored_hash):
                    hashed_password = security.hash_password(newPassword)
                    replacement_query = 'UPDATE user SET master_password_hash = %s WHERE username = %s;'
                    backend.run_query(replacement_query, (hashed_password, username.lower()))
                    return True
            return False
        except Exception as e:
            print(f"An error occurred: {e}")

    def nuke_account(self, username, password):
        """
        Deletes a user account and all associated passwords after verifying credentials.

        :param username: Username to delete
        :param password: Master password for verification
        :return: True if account deleted, False otherwise
        """
        hash_query = "select master_password_hash, encryption_key from user where username = %s;"
        hashed_pw = backend.run_query(hash_query, (username.lower(),))

        if hashed_pw:
            stored_hash = hashed_pw[0][0]
            encrypted_key_b64 = hashed_pw[0][1]
            encryption_key = base64.b64decode(encrypted_key_b64)
            security = sec.Security_and_Encryption(key=encryption_key)
            if security.verify_hashed_password(password, stored_hash):
                query2 = "DELETE FROM user WHERE username = %s;"
                query3 = "DELETE FROM account_password WHERE username = %s;"

                backend.run_query(query3, (username.lower(),))
                backend.run_query(query2, (username.lower(),))
                return True
            else:
                print("Username or password not found.")
                return False
        else:
            print("Username or password not found.")
            return False
    
    def create_key(self):
        """
        Generates a random 16-byte encryption key.

        :return: Bytes object representing the key
        """
        key = token_bytes(16)
        return key
    
    def recover_username(self, email):
        """
        Recovers and prints the username(s) associated with an email.

        :param email: Email address to search for
        """
        query = 'SELECT username FROM user WHERE user_email = %s;'
        username = backend.run_query(query, (email.lower(),))

        if username:
            for tuple in username:
                for name in tuple:
                    print(f'Your username is {name}')
        else:
            print('No results found')