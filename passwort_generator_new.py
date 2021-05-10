import secrets
import string

x = int(input("Please enter the password length: ")) #length of the password
chars = string.digits + string.ascii_letters + string.punctuation

print("".join(secrets.choice(chars) for _ in range(x)))
