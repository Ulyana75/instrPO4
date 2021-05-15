from LU_decomposition import get_LU_decomposition
from utilits import *


def solve(a: csr_matrix, b: csr_matrix):
    L, U = get_LU_decomposition(a)
    n = L.shape[0]
    y = csr_matrix(np.zeros(n))
    x = csr_matrix(np.zeros(n))
    y[0, 0] = b[0, 0]
    for i in range(1, n):
        s = 0
        for k in range(i):
            s += L[i, k] * y[0, k]
        y[0, i] = b[0, i] - s
    x[0, n - 1] = y[0, n - 1] / U[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for k in range(i + 1, n):
            s += U[i, k] * x[0, k]
        x[0, i] = (y[0, i] - s) / U[i, i]
    return x


if __name__ == "__main__":
    a = generate_random_matrix_sparse(2)
    b = [random.random() * 100 for i in range(2)]
    x = solve(csr_matrix(a), csr_matrix(b))
    print(check_SLAU_solution(a.todense(), x.todense(), np.array([b])))

