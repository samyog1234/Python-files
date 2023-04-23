def enter_message():
    try:
        while True:
            d_or_e=input("Would you like to encrypt (e) or decrypt (d): ")

            if d_or_e=="d" or d_or_e =="e":
                message=input("What message would you like to encrypt:")
                uppermessage=message.upper()
                while True:
                    try:
                        shift=int(input("What is the shift number:"))
                        print(d_or_e,uppermessage,shift)
                        break
                    except ValueError:
                        print("Invalid Mode")
                break
            else:
                print("Invalid Mode")
    except:
        pass
        return uppermessage,shift