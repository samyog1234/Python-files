def welcome():
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher.")

def enter_message():
    while True:
        d_or_e = input("Would you like to encrypt (e) or decrypt (d): ")

        if d_or_e == "d" or d_or_e == "e":
            source = input("Would you like to input your message via file (f) or console (c)? ")
            if source == "f":
                while True:
                    try:
                        file_name = input("Please enter the file name: ")
                        with open(file_name, "r") as f:
                           upper_message = f.read().upper()
                        break
                    except FileNotFoundError:
                        print("File not found. Please try again.")
                break
            elif source == "c":
                upper_message = input("What message would you like to encrypt/decrypt: ").upper()
                break
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please try again.")

    while True:
        try:
            shift = int(input("What is the shift number: "))
            if shift > 26:
                shift %= 26
            return upper_message, shift, d_or_e
        except ValueError:
            print("Invalid input. Please try again.")

def encrypt(upper_message, shift):
    encrypted_text = ""
    for char in upper_message:
        if char.isalpha():
            encrypting_value = ord(char) + shift
            if char.isupper():
                if encrypting_value > ord('Z'):
                    encrypting_value -= 26
            else:
                if encrypting_value > ord('z'):
                    encrypting_value -= 26
            encrypted_text += chr(encrypting_value)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(upper_message, shift):
    decrypted_text = ""
    for char in upper_message:
        if char.isalpha():
            decrypted_value = ord(char) - shift
            if char.isupper():
                if decrypted_value < ord("A"):
                    decrypted_value += 26
            else:
                if decrypted_value < ord("a"):
                    decrypted_value += 26
            decrypted_text += chr(decrypted_value)
        else:
            decrypted_text += char
    return decrypted_text

welcome()
while True:
    upper_message, shift, d_or_e = enter_message()

    if d_or_e == "e":
        encrypted_text = encrypt(upper_message, shift)
        print("Encrypted message:", encrypted_text)
    elif d_or_e == "d":
        decrypted_text = decrypt(upper_message, shift)
        print("Decrypted message:", decrypted_text)

    yes_or_no = input("Would you like to encrypt or decrypt another message? (y/n): ")
    if yes_or_no.lower() == "n":
        print("Thanks for using the program, goodbye!")
        break
    else:
        continue

