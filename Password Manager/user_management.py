import backend_sql as sql
import random
import Security_and_Encryption as sec



class UserManagement():

    

    def create_user(self, username, masterPassword):

        try:
            random_tag = random.randint(0,5000)

            new_username = username + '#' + str(random_tag)

            user_list = []
            username_query = 'select username from user;'

            query_result = sql.run_query(username_query,)

            for tuple in query_result:
                for element in tuple:
                    user_list.append(element)

            for _ in range(1000): 
                random_tag = random.randint(0, 5000)
                new_username = username + '#' + str(random_tag)
                if new_username not in user_list:
                    break
            else:
                raise Exception("Failed to generate a unique username")
                    

            hashed_password = sec.hash_password(masterPassword)

            query = 'INSERT INTO user (username, master_password_hash, encryption_key) VALUES (%s, %s, %s);'
            
            sql.run_query(query, (new_username, hashed_password, None))

            return True
        except Exception as e:
            print(f"An error occurred: {e}")
        

    def log_in(self, username, masterPassword):

        try:
            username_query = 'SELECT master_password_hash FROM user WHERE username = %s;'
            result = sql.run_query(username_query, (username,))
            if result:
                stored_password_hash = result[0][0]
                if sec.verify_hashed_password(masterPassword, stored_password_hash):
                    print('Login successful!')
                    return True
                else:
                    print('Username or password incorrect')
                    return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False



    def changeMasterPassword(self, username, oldPassword, newPassword):
        try:
            query = 'SELECT master_password_hash FROM user WHERE username = %s;'
            result = sql.run_query(query, (username,))
            if result:
                stored_hash = result[0][0]
                if sec.verify_hashed_password(oldPassword, stored_hash):
                    hashed_password = sec.hash_password(newPassword)
                    replacement_query = 'UPDATE user SET master_password_hash = %s WHERE username = %s;'
                    sql.run_query(replacement_query, (hashed_password, username))
                    return True
            return False
        except Exception as e:
            print(f"An error occurred: {e}")

    def nuke_account(self, username, password):

        hash_query = "select master_password_hash from user where username = %s;"
        hashed_pw = sql.run_query(hash_query, (username,))

        if hashed_pw:
            stored_hash = hashed_pw[0][0]
            if sec.verify_hashed_password(password, stored_hash):
                query2 = "DELETE FROM user WHERE username = %s;"
                query3 = "DELETE FROM account_password WHERE username = %s;"

                sql.run_query(query3, (username,))
                sql.run_query(query2, (username,))
                return True
            else:
                print("Username or password not found.")
                return False
        else:
            print("Username or password not found.")
            return False