# nume=10
# deno=0

# try:
#     result=nume/deno
#     print(result)
# except ZeroDivisionError:
#     print("Zero division error")

# try:
#     with open("example.txt","r") as file:
#         data=file.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("File cannot access")
# except Exception as e:
#     print(e)

# try:
#     with open("example.txt","r") as file:
#         data=file.read()
#         print(data)
# except Exception as e:
#     print(e)

# def divide(x,y):
#     if y==0:
#         raise ValueError("Cannot divided by 0")
#     return(x/y)

# # try:
# #     result=divide(10,0)
# #     print(result)
# # except ValueError as e:
# #     print(e)
    
# try:
#     result=divide(10,0)
#     print(result)
# except ValueError as e:
#     pass

def Divide(num1,num2):
    try:
        result=num1/num2
    except ZeroDivisionError:
        print("it is infinity so computer cannot solve")
    else:
        print(f"The division between {num1} and {num2} is equal to {result}")

Divide(10,2)
