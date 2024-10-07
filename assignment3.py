import numpy as np 
def finite_difference(n):
    main_diagonal_matrix = -2*np.eye(n)
    upper_diagonal_matrix =np.eye(n,k=1)
    lower_diagonal_matrix = np.eye(n,k=-1)
    final_matrix =(main_diagonal_matrix + upper_diagonal_matrix+ lower_diagonal_matrix)
    return final_matrix
print(finite_difference(5))