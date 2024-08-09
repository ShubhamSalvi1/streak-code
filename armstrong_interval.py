lower = int(input("Enter the lower end of the range: "))
upper = int(input("Enter the upper end of the range: "))
for x in range(lower,upper):
    x_str = str(x)
    x_len = len(x_str)
    sum = 0
    for digits in x_str:
        sum+=int(digits)**len(x_str)
    if sum == x:
        print(x)
    