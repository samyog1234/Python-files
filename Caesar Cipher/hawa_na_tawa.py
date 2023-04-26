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
            mode, message = enter_message()
        elif source == 'f':
            filename = input("Enter filename: ")
            message = read_file(filename)
            if message is not None:
                mode = input("Enter mode (e for encrypt, d for decrypt): ")
        else:
            print("Invalid input. Please try again.")
            continue

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

        save_to_file = input("Do you want to save the result to a file? (y/n) ")
        if save_to_file.lower() == 'y':
            filename = input("Enter filename: ")
            if mode == 'e':
                write_file(filename, encrypted_message)
                print("Encrypted message saved to '{}'.".format(filename))
            else:
                write_file(filename, decrypted_message)
                print("Decrypted message saved to '{}'.".format(filename))

        another_message = input("Do you want to process another message? (y/n) ")

    print("Thank you for using the Caesar Cipher program!")


if __name__ == '__main__':
    main()

