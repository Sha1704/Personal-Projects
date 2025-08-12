import backend_sql as sql
import Menus as menu
from user_management import UserManagement as user
from Password_Storage_and_Retrieval import StorageAndRetrieval as SnR
from Extras import Extra
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    database_host = os.getenv("DB_HOST")
    database_user = os.getenv("DB_USER")
    database_password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_DATABASE")

    # Enter into field below (host, user, password, database)
    sql_class = sql.Backend(database_host, database_user, database_password, database)
    user_management_class = user()
    password_Storage_and_Retrieval_class = SnR()
    extras_class = Extra()

    sql_class.run_query('use password_manager;')

    print("Welcome to the password manager! \n")

    try:
        while True:
            default_input = int(input(menu.default_menu()))

            if default_input == 999:
                print("Thank you for using the password manager. \n")
                print("Goodbye! \n")
                break

            while default_input not in [1, 2]:
                print("Please choose a valid option (1 or 2) \n")
                default_input = int(input(menu.default_menu()))
            
            if default_input == 1:
                username_create_user = str(input("Enter your username:"))
                masterPassword_create_user = input("Enter your Master password:")
                created = user_management_class.create_user(username_create_user,masterPassword_create_user)

                if created:
                    print("User created.")
                else:
                    print("Could not create user")

            elif default_input == 2:
    
                login_menu = None
                

                username = input("Enter your username:")
                masterPassword_login = input("Enter your Master password:")
                
                try:
                    logged_in, key = user_management_class.log_in(username, masterPassword_login)
                except TypeError as e:
                    print(f'Your username or master password is wrong')
                    continue


                if not logged_in or key is None:
                    print('Invalid username or password')
                    continue

                if logged_in:

                    while True:
                        login_menu = int(input(menu.login_menu()))

                        if login_menu == 999:
                            print("Logged out \n")
                            break

                        while login_menu not in range(1, 8):
                            print("Please choose a valid option (between 1 to 7)")
                            login_menu = int(input(menu.login_menu()))

                        if login_menu == 1:
                            #change master password
                            #changeMasterPassword(self, username, oldPassword, newPassword)
                            
                            username_change_master_password = input("Enter your username: ")
                            oldPassword = input("Enter your old password: ")
                            newPassword_change_master_password = input("Enter your new password: ")

                            pw_changed = user_management_class.changeMasterPassword(username_change_master_password, oldPassword, newPassword_change_master_password)

                            if pw_changed:
                                print("password changed sucessfully")
                            else:
                                print("unable to change password")

                        elif login_menu == 2:
                            #add password

                            url_add_password = ''
                            notes_add_password = ''
                            url_add_password_self = ''
                            notes_add_password_self = ''

                            password_menu_input = int(input(menu.add_password_menu()))

                            while password_menu_input < 1 or password_menu_input > 2:
                                password_menu_input = input("Choose a valid option (1 or 2): ")

                            if password_menu_input == 1:

                                pw_length = int(input("What is the desired length of you password (Enter a number):- "))

                                generated_password = extras_class.generate_strong_password(pw_length)

                                print(f"Your generated password is {generated_password}")
                                print()

                                accountName_add_password = input("Enter the name of the account you want to add: ")
                                account_username_add_password = input("Enter the account username/email: ")

                                url_input = input("Do you want to add a url (enter y/n) :- ").lower()
                                while url_input != 'y' and url_input != 'n':
                                    url_input = input("Enter y/n :- ").lower()
                                if url_input == 'y':
                                    url_add_password = input("Enter url: ")

                                note_input = input("Do you want to add a note (enter y/n) :- ").lower()
                                while note_input != 'y' and note_input != 'n':
                                    note_input = input("Enter y/n :-").lower()
                                if note_input == 'y':
                                    notes_add_password = input("Add note here: ")

                                added = password_Storage_and_Retrieval_class.addPassword(key, accountName_add_password, username, account_username_add_password, generated_password, url_add_password, notes_add_password)

                                if added:
                                    print("Password added.")
                                    print("Generated password used.")
                                else:
                                    print("Unable to add password")
                                
                            elif password_menu_input == 2:

                                accountName_add_password_self = input("Enter the name of the account you want to add: ")
                                account_username_add_password_self = input("Enter the account username/email: ")
                                password_add_password_self = input("Enter your password: ")

                                url_input = input("Do you want to add a url (enter y/n) :- ").lower()
                                while url_input != 'y' and url_input != 'n':
                                    url_input = input("Enter y/n :- ").lower()
                                if url_input == 'y':
                                    url_add_password_self = input("Enter url: ")

                                note_input = input("Do you want to add a note (enter y/n) :- ").lower()
                                while note_input != 'y' and note_input != 'n':
                                    note_input = input("Enter y/n :- ").lower()
                                if note_input == 'y':
                                    notes_add_password_self = input("Add note here: ")

                                added = password_Storage_and_Retrieval_class.addPassword(key, accountName_add_password_self, username, account_username_add_password_self, password_add_password_self, url_add_password_self, notes_add_password_self)
                                
                                if added:
                                    print("Password added.")
                                    print("Generated password used.")
                                else:
                                    print("Unable to add password")


                        elif login_menu == 3:
                            #get password

                            accountName_get_password = input("What account do you want to get the password for? ")

                            pw = password_Storage_and_Retrieval_class.getPassword(accountName_get_password, username, key)

                            if pw != None:
                                print(f"Your password for {accountName_get_password} is: {pw}")
                            else:
                                print("Unable got get Password for that account (please check to make sure that that account exists)")

                            

                        elif login_menu == 4: 
                            #get all password

                            master_password_get_all_password = input("Enter your master password: ")

                            print()

                            try:
                                result = password_Storage_and_Retrieval_class.getAllPasswords(username, master_password_get_all_password, key)
                            except TypeError as e:
                                print(f'You have no saved password in your account, please add a password')
                                continue
                           

                        elif login_menu == 5:
                            #update password

                            accountName_update_password = input("Enter the name of the account you want to update the password of: ")
                            newPassword_update_password =input("Enter the new password: ")

                            update = password_Storage_and_Retrieval_class.updatePassword(username, accountName_update_password, newPassword_update_password, key)

                            if update:
                                print("Password updated sucessfully")
                            else:
                                print("Could not update password, account name might be wrong")


                        elif login_menu == 6:
                            #delete password

                            accountName_delete_password = input("Enter the name of the account you want to remove: ")
                            username_delete_password = input("Enter your password manager username: ")
                            validate = input(f"Are you sure you want to delete your {accountName_delete_password} account, this action cannot be undone. (enter y/n): ").strip().lower()

                            while validate != 'y' and validate != 'n':
                                validate = input("Enter \"y\" or \"n\": ")
                            
                            if validate == 'y':
                                deleted = password_Storage_and_Retrieval_class.removeAccount(accountName_delete_password, username_delete_password)
                            
                            if deleted:
                                print('Account removed successfully')
                            else:
                                print("Could not remove account, account information might be wrong")
                          

                        elif login_menu == 7:
                            # nuke account

                            username_nuke_account = input("Enter your username: ")
                            password_nuke_account = input("Enter your master password: ")

                            red_button = user_management_class.nuke_account(username_nuke_account, password_nuke_account)

                            if red_button:
                                print("Account deleted")
                                break
                            else:
                                print("Could not delete account")
                            
                else:
                    print("Could not log in \n")
                   
    except ValueError as e:
        print("Invalid input. You entered a wrong input type, please start over.")
        print(e)


if __name__ == "__main__":
    main()
