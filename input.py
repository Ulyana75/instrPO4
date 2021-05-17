import numpy as np
from LU_decomposition import get_LU_decomposition, get_reverse_matrix
from scipy.sparse import csr_matrix
from SLAU import solve

"""
Input data from user
"""

n = int(input("Enter dim of matrix: "))
print("Enter matrix:")
a = np.zeros((n, n))
for i in range(n):
    b = list(map(float, input().split()))
    for j in range(n):
        a[i][j] = b[j]

print("LU decomposition:")
L, U = get_LU_decomposition(csr_matrix(a))
print(L.toarray(), '\n')
print(U.toarray(), '\n')

print("Reverse matrix:")
print(get_reverse_matrix(csr_matrix(a)).toarray(), '\n')

print("Enter vector b:")
b = list(map(float, input().split()))

print("Solution vector:")
x = solve(csr_matrix(a), csr_matrix(b))
print(x.toarray())
