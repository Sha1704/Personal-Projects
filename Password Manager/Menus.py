def default_menu():
    """
    Returns the default menu string for main options.
    """
    str = 'Select from the following options: \n' \
    '1 - Create new account \n' \
    '2 - Login \n' \
    '3 - Recover username \n' \
    'Enter 999 to quit \n' \
    'Your choice :- '

    return str

def login_menu():
    """
    Returns the menu string for logged-in user options.
    """
    string = 'Select from the following options: \n' \
    '1 - Change master password \n' \
    '2 - Add password \n' \
    '3 - Get password \n' \
    '4 - Get all passwords \n' \
    '5 - Update password \n' \
    '6 - remove account from password manager \n' \
    '7 - Delete your password manager account \n' \
    '999 - log-out \n' \
    'Your choice :- '

    return string

def add_password_menu():
    """
    Returns the menu string for adding a password.
    """
    menu = 'Select from the following options: \n' \
    '1 - Generate strong password \n' \
    '2 - Use your own password \n' \
    'Your choice :- '

    return menu

