count = 0
for x in range(1,10):
    if(x%2==0):
        print(x)
        count+= 1
    else: 
        exit
print("We have ", count, " even numbers")

