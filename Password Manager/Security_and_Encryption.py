from Crypto.Cipher import AES
import base64
import bcrypt


class Security_and_Encryption:

    KEY_FILE = "encryption.key"

    def __init__(self, key = None):
        if key is None:
            raise ValueError("Encryption key must be provided.")
        self.key = key
    
    def encryptData(self,message):
        cipher = AES.new(self.key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(message.encode('UTF-8'))
        return (base64.b64encode(nonce),
                base64.b64encode(ciphertext),
                base64.b64encode(tag))
    
    def decryptData(self, nonce_b64, cipher_text_b64, tag_b64, key): 

        nonce = base64.b64decode(nonce_b64)
        cipher_text = base64.b64decode(cipher_text_b64)
        tag = base64.b64decode(tag_b64)


        cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
        plain_text = cipher.decrypt(cipher_text)
        try:
            cipher.verify(tag)
            return plain_text.decode('UTF-8')
        except ValueError as e:
            print(f"Error: {e}")
            return None
        
    def hash_password(self, password_to_hash):
        generated_salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password = password_to_hash.encode(), salt = generated_salt)
        
        return hashed_password
    
    def verify_hashed_password(self, user_password, hash_password):
        if bcrypt.checkpw(password = user_password.encode(), hashed_password = hash_password.encode()):
            return True
        else:
            return False
        
    
        
