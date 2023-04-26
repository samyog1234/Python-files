def welcome():
    """Prints a welcome message to the user."""
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.\n")


def enter_message():
    """Prompts the user for the mode (encrypt/decrypt) and the message."""
    mode = ''
    while mode != 'e' and mode != 'd':
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode != 'e' and mode != 'd':
            print("Invalid mode. Please enter 'e' to encrypt or 'd' to decrypt.")

    message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt")).upper()

    return mode, message


def encrypt(message, shift):
    """Encrypts the given message using the Caesar Cipher algorithm."""
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)  # Shifts the character by the given shift
            encrypted_message += shifted_char
        else:
            encrypted_message += char  # Leaves non-alphabetic characters unchanged

    return encrypted_message


def decrypt(message, shift):
    """Decrypts the given message using the Caesar Cipher algorithm."""
    decrypted_message = ''
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)  # Shifts the character by the given shift
            decrypted_message += shifted_char
        else:
            decrypted_message += char  # Leaves non-alphabetic characters unchanged

    return decrypted_message


def read_file(filename):
    """Reads content from a file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            mode = 'e' if filename.endswith('.enc') else 'd'  # Infers the mode from the file extension
            return mode, content
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
        source = ''
        while source != 'c' and source != 'f':
            source = input("Enter 'c' to input from console, or 'f' to input from file: ").lower()
            if source != 'c' and source != 'f':
                print("Invalid input. Please enter 'c' or 'f'.")

        if source == 'c':
            mode, message = enter_message()
        else:
            filename = input("Enter filename: ")
            mode, message = read_file
