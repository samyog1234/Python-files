def wellcome():
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    while True:
        d_or_e = input("Would you like to encrypt (e) or decrypt (d): ")

        if d_or_e == "d" or d_or_e == "e":
            message = input("What message would you like to encrypt:")
            uppermessage = message.upper()
            while True:
                try:
                    shift = int(input("What is the shift number:"))
                    return uppermessage, shift, d_or_e
                except ValueError:
                    print("Invalid Mode")
        else:
            print("Invalid Mode")


def encrypt(uppermessage, shift):
    encrypted_text = ""
    for char in uppermessage:
        if char.isalpha():
            encrypting_value = ord(char) + shift
            if char.isupper():
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
            decrypted_value = ord(char) - shift
            if char.isupper():
                if decrypted_value < ord("A"):
                    decrypted_value += 26
            decrypted_text += chr(decrypted_value)
        else:
            decrypted_text += char
    return decrypted_text


wellcome()
uppermessage, shift, d_or_e = enter_message()

if d_or_e == "e":
    encrypted_text = encrypt(uppermessage, shift)
    print("Encrypted message:", encrypted_text)
elif d_or_e == "d":
    decrypted_text = decrypt(uppermessage, shift)
    print("Decrypted message:", decrypted_text)
