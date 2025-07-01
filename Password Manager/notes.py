'''
To do:

password manager app

debugg

unique username issue (i add a suffix to username but user don't know what the suffix is fix? python lib)
hash password issue in user management

'''

'''
Done:

Security & Encryption:
encryptData(message)
decryptData(nonce, cypher_text, tag)

user management:
create_user(username, masterPassword) : add username and password to sql (hash password before storing, check if username exists in database)
log_in(username, masterPassword) : check if username and password is in sql, act accordingly 
changeMasterPassword(username, oldPassword, newPassword) : check if username and old password match, if so ask for new password and store it (dont forget to hash)

Extras:
generateStrongPassword(length)

Password Storage & Retrieval:
addPassword(accountName, username, password, url, notes) : store all into sql
getPassword(accountName)
getAllPasswords(Master_password)
updatePassword(accountName, newPassword)
deletePassword(accountName)

main:
print menu (create new account, login)
    if login (changeMasterPassword, addPassword, getPassword, getAllPasswords, updatePassword, deletePassword)
        if addPassword(generateStrongPassword, use your own password)
'''