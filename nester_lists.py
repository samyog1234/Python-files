k=0
sum=0
class_grades=[[85,91,89],[78,81,86],[62,75,77],[62,75,77]]
while k<len(class_grades):
    sum+=class_grades[k][0]
    k+=1
    average=sum/float(len(class_grades))
print(average)

# k = 0
# sum = 0
# class_grades = [[85, 91, 89], [78, 81, 86], [62, 75, 77],[62, 75, 77]]
# while k < len(class_grades):
#     sum = sum + class_grades[k][0]
#     k +=1
#     avergae = sum/float(len(class_grades))
#     print(avergae)
