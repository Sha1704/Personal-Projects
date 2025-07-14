import string
import secrets

class Extra:
    def generate_strong_password(length):
        password = ''
        alphabet  = string.ascii_letters + string.digits + string.punctuation
        for i in range (length):
            password += secrets.choice(alphabet)
        return password