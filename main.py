from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)


def call_key():
    return open("pass.key", "rb").read()


key = call_key()

name = input("Enter Your Name:\n")
password = input("Enter a password:\n")
message = input("Enter the message you want to encode:\n")

a = Fernet(key)

slogan = message.encode()
coded_slogan = a.encrypt(slogan)

pub_key_slogan = name.encode()
pub_key = a.encrypt(pub_key_slogan)

pri_key_slogan = password.encode()
pri_key = a.encrypt(pri_key_slogan)

with open("publickey.json", 'wb') as f:
    f.write(pub_key)

with open("message.json", 'wb') as f:
    f.write(coded_slogan)

print("Here is your Private key:", pri_key, "Save this and don't show it to someone")
