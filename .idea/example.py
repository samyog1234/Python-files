# f = open('example.txt','r')
# multiple_lines = f.readlines()
# print("multpli line==>",multiple_lines)
# f.close()
# with open("example.txt","r") as A:
#     one_line= A.readline()
#     multiple_lines=A.readlines()
#     print("Single Line using with ==> \n",one_line)
#     print("Multi Line using with==>", multiple_lines)
# with open("example.txt","w") as A:
#     A.write("This is not a mistake")
#     if __name__ == "__main__":
#         file_handling()
name=input("Enter your name:")
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.strip())
print(name.split())
print(name.find("sam"))
print(name.startswith("wow"))
print(name.endswith("no"))






