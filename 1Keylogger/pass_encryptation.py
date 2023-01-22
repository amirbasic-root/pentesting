import os

from cryptography.fernet import Fernet

from config.keylogger_config import EMAIL_PASSWORD, ENC_PASS_FILENAME, KEY_FILENAME


def generate_key(file_name=KEY_FILENAME):
    key = Fernet.generate_key()
    with open(file_name, 'wb') as file:
        file.write(key)


def generate_encrypted_key(key, file_name=ENC_PASS_FILENAME):
    with open(file_name, 'wb') as file:
        fernet_key = Fernet(key)
        encrypted_password = fernet_key.encrypt(EMAIL_PASSWORD)
        file.write(encrypted_password)
        file.close()


def get_key(file_name=KEY_FILENAME):
    if not os.path.exists(file_name):
        generate_key(file_name)
        
    return open(file_name, 'rb').read()


def get_encrypted_key(key_file_name=KEY_FILENAME, file_name=ENC_PASS_FILENAME):
    if not os.path.exists(file_name):
        key = get_key(key_file_name)
        generate_encrypted_key(key, file_name)
        
    return open(file_name, 'rb').read()


def decrypt_password(encrypted_password, key_filename=KEY_FILENAME):
    key = get_key(key_filename)
    fernet_key = Fernet(key)
    password = fernet_key.decrypt((encrypted_password)).decode()
    return password



if __name__ == '__main__':
    get_encrypted_key()
