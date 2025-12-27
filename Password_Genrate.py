import random
import string

# Taking input from user
length = int(input("Enter desired password length: "))

# Characters to use for password
characters = string.ascii_letters + string.digits + string.punctuation

# Generating password
password = ""
for i in range(length):
    password += random.choice(characters)

# Displaying password
print("Generated Password:", password)
