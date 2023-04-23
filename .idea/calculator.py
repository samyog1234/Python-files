num=0
# while num<1:
#     num_1=int(input("Enter a number to make its multiplication table: "))
#     for i in range(1,11):
#         print(f"{num_1} * {i} = {num_1*i}")
while num<1:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    sign=input("Enter sign to calculate: ")
    if sign =="-":
        print(num1-num2)
    elif sign=="+":
        print((num1+num2))
    elif sign =="*":
        print(num1*num2)
    elif sign=="**":
        print(num1**num2)
    else:
        print(num1/num2)
