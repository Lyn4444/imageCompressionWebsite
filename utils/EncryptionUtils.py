from cryptography.fernet import Fernet


class Encryption:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        encoded_message = message.encode()
        f = Fernet(self.key)
        encrypted_message = f.encrypt(encoded_message)
        return encrypted_message

    def decrypt(self, encrypted_message):
        f = Fernet(self.key)
        decrypted_message = f.decrypt(encrypted_message)
        message = decrypted_message.decode()
        return message
