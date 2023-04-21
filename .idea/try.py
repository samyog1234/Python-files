# # number 1 using while
# num=1
# sum=0
# while num<10:
#     print(num)
#     num+=1
# #number 1 using for
# for i in range(1,10):
#     print(i)
#     i+=1
# # number 2 using for and simple code
# for i in range(1,16,2):
#     print(i)
#     i+=1
# #number 2 using hard code
# for i in range(1,16):
#     if i%2!=0:
#         print(i)
# #number 3 only one output
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)
# #number 3 with many outputs
# sum=0
# for i in range(1,11):
#     sum+=i
#     print(sum)
# #number 4 
# multi_num=int(input("Enter the positive number: "))
# if multi_num<0:
#     print("Number must be positive: ")
# else:
#     for i in range(1,11):
#         print(multi_num,"*",i,"=",)
# # number 6
# num=int(input("Enter number to know its factorial: "))  
# if num<0:
#     print("A negative number can't have its factorial")
# elif num==0:
#     print("The factorial of 0 is 1")
# else:
#     factorial=1
#     for i in range(1,num+1):
#         factorial=factorial*i
# print(factorial)
# #number 7
# negative_count=0
# zero_count=0
# positive_count=0
# while True:
#     pnz_count=float(input("Enter a number or enter 0.1 to stop: "))
#     if pnz_count==0.1:
#         break
#     elif pnz_count<0:
#         negative_count+=1
#     elif pnz_count==0:
#         zero_count+=1
#     elif pnz_count>0:
#         positive_count+=1

# print("The negative is",negative_count,"The zero is",zero_count,"The positive is",positive_count)
# #number 7
# limit=int(input("Enter an limit for Fibonacci series: "))
# num1=0
# num2=1
# while num1+num2<=limit:
#     num3=num1+num2
#     print(num3)
#     num1=num2
#     num2=num3
# #number 10
# multiplication=0
# for i in range(1,21):
#     if i%5==0:
#         i*=i
# # print(i)
# for i in range(1,11):
#     print("2 *",i,"=",i*2,end="          ")
#     print("5 *",i,"=",i*5,end="          ")
#     print("7 *",i,"=",i*7)
