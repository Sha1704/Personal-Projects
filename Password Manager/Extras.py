import string
import secrets
import random

class Extra:
    def generate_strong_password(self, length, numbers = True, special_characters = True):

        if length < (numbers + special_characters):
            print("Length too short to include required characters")
            return False
            
        
        
        alphabet  = string.ascii_letters
        digits = string.digits
        punctuation = string.punctuation
        password_char = []

        if numbers:
            password_char.append(secrets.choice(digits))
            alphabet += digits
        if special_characters:
            password_char.append(secrets.choice(punctuation))
            alphabet += punctuation

        while len(password_char) < length:
            password_char.append(secrets.choice(alphabet))

        random.shuffle(password_char)

        return ''.join(password_char)