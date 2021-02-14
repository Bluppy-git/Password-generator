import random, string

random.seed()
inhalt = ''

z = input("Laenge: ")
laenge = int(z)
klein = input("Kleinbuchstabe (j/n): ")
gross = input("Grossbuchstaben (j/n): ")
zahl = input("Zahlen (j/n): ")
zeichen = input("Sonderzeichen (j/n): ")

if klein == 'j':
    inhalt += string.ascii_lowercase
if gross == 'j':
    inhalt += string.ascii_uppercase
if zahl == 'j':
    inhalt += string.digits
if zeichen == 'j':
    inhalt += string.punctuation

pw = ''.join(random.choice(inhalt) for i in range(laenge))
print("Passwort:", pw)
