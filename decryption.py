from cryptography.fernet import Fernet


def call_key():
    return open("pass.key", "rb").read()


def decryp_msg():
    return open("message.json", "rb").read()


coded_slogan = decryp_msg()
print(coded_slogan)
key = call_key()
b = Fernet(key)
decoded_slogan = b.decrypt(coded_slogan)
print(decoded_slogan)
