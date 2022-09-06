import random


lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = lowercase_alphabet.upper()
numbers = "0123456789"
special_characters = "!?#$%^&*()+@-"

# By default you need to initialize set with lowercase alphabet
characters_set = # -- * Your code here * --

print("By default password creates from english alphabet in lower case.")

answer = input("Do you want to add upper case letters to your random password? YES/NO: ")
while # -- * Your code here * --:
    answer = input("You typed wrong asnwer. Please enter YES or NO: ")
    # If positive answer than add new set of characters to current set
    if # -- * Your code here * --
else:
    # If positive answer than add new set of characters to current set
    if # -- * Your code here * --
        
answer = input("Do you want to add numbers to your random password? YES/NO: ")
while not ((answer == "YES") or (answer == "NO")):
    answer = input("You typed wrong asnwer. Please enter YES or NO: ")
    # If positive answer than add new set of characters to current set
    if # -- * Your code here * --
else:
    # If positive answer than add new set of characters to current set
    if # -- * Your code here * --

answer = input("Do you want to add special characters to your random password? YES/NO: ")
while not ((answer == "YES") or (answer == "NO")):
    answer = input("You typed wrong asnwer. Please enter YES or NO: ")
    # If positive answer than add new set of characters to current set
    if # -- * Your code here * --
else:
    # If positive answer than add new set of characters to current set
    if # -- * Your code here * --

print("Set of symbols to create password:", characters_set, end = "\n\n")
        
print("Password should be not lower than 6 symbols and not more than 32")

password_length = int(input("Enter password length: "))
# If user entered wrong number program asks again
while # -- * Your code here * --
    password_length = int(input("You typed wrong number. Enter number between 6 and 32: "))

password = ""
while # -- * Your code here * --:
    # Take one random character out of characters set
    random_character = # -- * Your code here * --
    # Add character to password
    # -- * Your code here * --

print("Random generated password:", password)

# Example of RESULT
# By default password creates from english alphabet in lower case.
# Do you want to add upper case letters to your random password? YES/NO: YES
# Do you want to add numbers to your random password? YES/NO: Nah
# You typed wrong asnwer. Please enter YES or NO: NO
# Do you want to add special characters to your random password? YES/NO: YES
# Set of symbols to create password: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?#$%^&*()+@-

# Password should be not lower than 6 symbols and not more than 32
# Enter password length: 100500
# You typed wrong number. Enter number between 6 and 32: 8
# Random generated password: Dac?uoHzI
