import string
import secrets
import random

class Extra:
    """
    Provides extra utilities, such as generating strong passwords.
    """
    def generate_strong_password(self, length, numbers = True, special_characters = True):
        """
        Generates a strong random password.

        :param length: Desired password length
        :param numbers: Whether to include numbers
        :param special_characters: Whether to include special characters
        :return: Generated password string or False if length too short
        """
        if length < (numbers + special_characters):
            print("Length too short to include required characters")
            return False
            
        alphabet  = string.ascii_letters
        digits = string.digits
        punctuation = string.punctuation
        password_char = []

        # Ensure at least one number and/or special character if requested
        if numbers:
            password_char.append(secrets.choice(digits))
            alphabet += digits
        if special_characters:
            password_char.append(secrets.choice(punctuation))
            alphabet += punctuation

        # Fill the rest of the password
        while len(password_char) < length:
            password_char.append(secrets.choice(alphabet))

        random.shuffle(password_char)

        return ''.join(password_char)