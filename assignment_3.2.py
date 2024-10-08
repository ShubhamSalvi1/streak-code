import numpy as np
def matrix_multiplication(n):
    X = np.array(range(1,2*(n**2)+1,2)).reshape((n,n))
    Y = np.array(range(2*n**2,0,-2)).reshape((n,n))
    Z= np.dot(X,Y)
    return Z
print(matrix_multiplication(3))