#doc-strings
def square(n):
    '''
    this function is meant to take the value of n and return its square
    '''
    print(n*n)
square(5)
#doc-strings have to be written below the defining of the function and above the main function body
print(square.__doc__) #to print the doc string literal