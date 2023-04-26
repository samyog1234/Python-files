def welcome():
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher.")

def enter_message():
    while True:
        d_or_e = input("Would you like to encrypt (e) or decrypt (d): ")

        if d_or_e == "d" or d_or_e == "e":
            message = input("What message would you like to encrypt:")
            uppermessage = message.upper()

            try:
                shift = int(input("What is the shift number:"))
                if d_or_e == "e":
                    encrypted_text = encrypt(uppermessage, shift)
                    print("Encrypted message:", encrypted_text)
                elif d_or_e == "d":
                    decrypted_text = decrypt(uppermessage, shift)
                    print("Decrypted message:", decrypted_text)
                    Yes_or_no = input("Would you like to encrypt or decrypt another message? (y/n): ")
                if Yes_or_no == "n":
                    print("Thanks for using the program, goodbye!")
                    return False
            except ValueError:
                print("Invalid Mode")
        else:
            print("Invalid Mode")


def encrypt(uppermessage, shift):
    encrypted_text = ""
    for char in uppermessage:
        if char.isalpha():
            encrypting_value = ord(char) + shift
            if encrypting_value > ord('Z'):
                encrypting_value -= 26
            encrypted_text += chr(encrypting_value)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(uppermessage, shift):
    decrypted_text = ""
    for char in uppermessage:
        if char.isalpha():
            decrypted_value = ord(char)-shift
            if decrypted_value < ord("A"):
                decrypted_value += 26
            decrypted_text += chr(decrypted_value)
        else:
            decrypted_text += char
    return decrypted_text

def read_file(filename):
    """Reads content from a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None


def write_file(filename, content):
    """Writes content to a file."""
    with open(filename, 'w') as file:
        file.write(content)


def main():
    """Main function that drives the program."""
    welcome()

    another_message = 'y'
    while another_message.lower() == 'y':
        source = input("Enter 'c' to input from console, or 'f' to input from file: ")
        if source == 'c':
            enter_message()
        elif source == 'f':
            filename = input("Enter filename: ")
            message = read_file(filename)
            if message is not None:
                mode = input("Enter mode (e for encrypt, d for decrypt): ")
                shift = 0
                while not shift:
                    try:
                        shift = int(input("What is the shift number (0-25)? "))
                        if not (0 <= shift <= 25):
                            print("Invalid shift number. Please enter a number between 0 and 25.")
                            shift = 0
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        shift = 0

                if mode == 'e':
                    encrypted_message = encrypt(message, shift)
                    print("Encrypted message: {}".format(encrypted_message))
                else:
                    decrypted_message = decrypt(message, shift)
                    print("Decrypted message: {}".format(decrypted_message))

                save_to_file = input("Do you want to save the result")
