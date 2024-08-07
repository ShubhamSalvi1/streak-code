#First method
# import math
# n = int(input("Enter the number: "))
# fact = math.factorial(n)
# if n>0:
#     print(fact)
# else:
#     print("Enter a positive integer.")
#Second method
num = int(input("Enter the number: "))
count=1
if num > 0:
    for x in range(1,num+1):
         count *= x
         
    print(count)
else:
    print("Invalid")

