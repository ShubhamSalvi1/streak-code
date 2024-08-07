x=int(input("Enter the number of terms you want: "))
a , b= 0 , 1
print(a, end=" ")
print(b, end=" ")
for i in range(2,x):
    next = a + b
    print(next, end=" ")
    a,b=b,next

