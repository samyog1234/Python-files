password=input("Enter an password:")

if len(password) <8 :
    print("The password must have 8 letters")

elif not any(char.isupper() for char in password):
    print("The password must have at least one upper case letter")

elif not any(char.islower() for char in password):
    print("The password must have at least one lower case letter")

elif not any(char.isdigit() for char in password):
    print("The password must have at least one digit")

else:
    print("The password is valid")



