import os

def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def encrypt(message, shift):
    result = ""
    for c in message:
        result += chr(ord(c) + shift)
    return result


def decrypt(message, shift):
    return encrypt(message, -shift)


def process_file(filename, mode, shift):
    with open(filename, 'r') as f:
        message = f.read()
    return encrypt(message, shift) if mode == "e" else decrypt(message, shift)


def main():
    welcome()

    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

        if mode not in ('e', 'd'):
            print("Invalid mode.")
            continue

        shift = input("What is the shift number: ")

        try:
            shift = int(shift)
        except ValueError:
            print("Invalid shift number.")
            continue

        if mode == 'e':
            filename = input("What file would you like to encrypt? ")
            if not os.path.isfile(filename):
                print("File not found:", filename)
                continue
            print("Encrypted message:", process_file(filename, mode, shift))
        elif mode == 'd':
            filename = input("What file would you like to decrypt? ")
            if not os.path.isfile(filename):
                print("File not found:", filename)
                continue
            print("Decrypted message:", process_file(filename, mode, shift))

        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message == "n":
            break


if __name__ == "__main__":
    main()
