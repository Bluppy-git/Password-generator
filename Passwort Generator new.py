import secrets
import string

x = 8 #the x is the number of letters your password will have

chars = string.digits + string.ascii_letters + string.punctuation
print("".join(secrets.choice(chars) for _ in range(x)))
