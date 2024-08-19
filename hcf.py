a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
def hcf(a,b):
    if a > b:
        smaller = b
    elif b>a:
        smaller = a
    else:
        print("The HCF is: ", a)
    for i in range(1, smaller+1):
        if(a%i==0) and (b%i==0):
            hcf=i
    return hcf
x=hcf(a,b)
print(x)

       