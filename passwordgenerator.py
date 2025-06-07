import random 
import string
import pyperclip
def generate_password(length=15):
    characters = random.choices(string.ascii_letters + string.digits + string.punctuation, k=length)
    password = ''.join(characters)
    return password
print("Welcome to the Password Generator!")
choice = input("Do you want to generate a password? (yes/no): ")
if choice == 'yes':
    password = generate_password()
    print("Your generated password is: " + password)
else:
    print("No password generated. Exiting the program.")
    exit()
copy = input("Do you want to copy the password to clipboard? (yes/no): ")
if copy == 'yes':
    pyperclip.copy(password)
    print("Password copied to clipboard.")
else :
    print("Password not copied to clipboard.")
    exit()
