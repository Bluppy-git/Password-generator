import random, string

random.seed()
content = ''

z = input("length: ")
lenght = int(z)
lowercase_letters = input("lowercase letters (y/n): ")
capital_letters = input("capital letters (y/n): ")
numbers = input("numbers (j/n): ")
special_characters = input("special characters (j/n): ")

if lowercase_letters == 'j':
    content += string.ascii_lowercase
if capital_letters == 'j':
    content += string.ascii_uppercase
if numbers == 'j':
    content += string.digits
if special_characters == 'j':
    content += string.punctuation

pw = ''.join(random.choice(inhalt) for i in range(laenge))
print("password:", pw)
