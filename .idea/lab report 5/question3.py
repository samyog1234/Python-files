positive_number=0
negative_number=0
sum_positive=0

print("Enter any positive and negative number and zero to stop:")
while True:
    p_user=int(input("Enter any integer: "))
    if p_user==0:
        break
    elif p_user>0:
        positive_number+=1
        sum_positive+=p_user
    else:
        negative_number+=1
print(f"You enter {positive_number} times positive numbers and {negative_number} times negative number")
print(f"The sum of positive numbers is {sum_positive}")
