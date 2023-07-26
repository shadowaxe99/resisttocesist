```python
from cryptography.fernet import Fernet
import os

class DataPrivacySecurity:
    def __init__(self):
        self.key = os.environ.get('SECRET_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, userData):
        encrypted_data = self.cipher_suite.encrypt(userData.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data

    def protectData(self, userData):
        encrypted_data = self.encrypt_data(userData)
        return encrypted_data

    def accessData(self, encrypted_data):
        decrypted_data = self.decrypt_data(encrypted_data)
        return decrypted_data
```