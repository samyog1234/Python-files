print("Welcome to ENQUIRY FORM ")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
qualification=input("Enter your major qualification: ")
cont_num=int(input("Enter your number to contact you: "))
address=input("Enter your full address: ")
email=input("Enter your email: ")
int_area=input("Enter your interested area: ")
description=input("Enter a description about your anything: ")
salary=int(input("Enter how much you want form this job: "))
if salary > 20000:
    print("your work experience must be at least 2 years")
    expe=int(input("Enter your experience year: "))
    if expe>2:
        print("you are shortlisted your enquiry has been recorded, we will notify you, thank you!!")
    else:
        print("your enquiry has been recorded, we will notify you, thank you!!")
else:
    print("your enquiry has been recorded, we will notify you, thank you!")