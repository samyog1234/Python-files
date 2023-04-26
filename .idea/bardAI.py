# Import the necessary libraries
import string

# Get the user input
text = input("Enter the text you want to encrypt: ")

# Get the shift value
shift = int(input("Enter the shift value: "))

# Create a mapping of the alphabet to the shifted alphabet
alphabet = string.ascii_lowercase
shifted_alphabet = alphabet[shift:] + alphabet[:shift]

# Encrypt the text
encrypted_text = ""
for letter in text:
    if letter in alphabet:
        encrypted_text += shifted_alphabet[alphabet.index(letter)]
    else:
        encrypted_text += letter

# Print the encrypted text
print("The encrypted text is:", encrypted_text)
