#fibonacci sequence using recursion in python 
n = int(input("Enter a number: "))
def fibo(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2) #using a defined function in its own function is called recursion
for i in range (0,n):
    print(fibo(i))