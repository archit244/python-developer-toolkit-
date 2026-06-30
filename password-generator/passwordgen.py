import random

character_pool = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:',.<>?/~`"

def include_or_not(var):
    include_var=""
    while True:   
        include_var=input(f"Include {var}? (y/n):").strip().lower()
        if include_var in ("y","n"):     
            return include_var
        else:
              print("invalid")
length=""
while True:
    length = input("Enter the length of password: ")
    try:
        length = int(length)
    except ValueError:
        print("Please enter a valid length.")
        continue
    if length>0:
         break

include_upper=include_or_not("Uppercase")
include_numbers=include_or_not("Numbers")
include_symbols=include_or_not("Symbols")

if include_upper=="y":
        character_pool+=UPPERCASE
if include_numbers=="y":
        character_pool+=NUMBERS
if include_symbols=="y":
        character_pool+=SYMBOLS

password=""
for _ in range (length):
    password+=random.choice(character_pool)
print(f"\nGenerated Password: {password}")