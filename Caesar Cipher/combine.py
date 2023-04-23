# def wellcome():
#     print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher.")


# def enter_message():
#     try:
#         while True:
#             d_or_e=input("Would you like to encrypt (e) or decrypt (d): ")

#             if d_or_e=="d" or d_or_e =="e":
#                 message=input("What message would you like to encrypt:")
#                 uppermessage=message.upper()
#                 while True:
#                     try:
#                         shift=int(input("What is the shift number:"))
#                         print(d_or_e,uppermessage,shift)
#                         break
#                     except ValueError:
#                         print("Invalid Mode")
#                 break
#             else:
#                 print("Invalid Mode")
#     except:
#         pass
#         return uppermessage,shift



# def encrypt():
#     upmess="hello"
#     dict_upmess={letter: upmess.ord("h") for letter in set(upmess)}
#     print(dict_upmess)
    
# encrypt()
# uppermessage="HELLO"
#     dict_uppermessage={letter: uppermessage.count(letter) for letter in set(uppermessage)}
#     print(dict_uppermessage)

# my_string = "HELLO"

# print(my_dict)


word = input("Enter a string: ")
shift=int(input("Enter a shift to make a shift:"))
word=word.capitalize()
letter_list=list(word)
while True:
    for char in word:
        orde=int(ord(char))
        if orde >90:
            orde-=25
            ch=chr(orde)
            print(ch)
        else:
            prin=(orde+shift)
            print(chr(prin))
            break









    

