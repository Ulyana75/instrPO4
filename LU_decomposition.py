from utilits import *
import warnings
warnings.simplefilter("error", RuntimeWarning)


def get_LU_decomposition(a: csr_matrix):
    n = int(a.shape[0])
    L = csr_matrix(np.zeros((n, n)))
    U = csr_matrix(np.zeros((n, n)))
    for j in range(n):
        L[j, j] = 1
    for i in range(n):
        for j in range(n):
            if i <= j:
                s = 0
                for k in range(i):
                    s += L[i, k] * U[k, j]
                U[i, j] = a[i, j] - s
            else:
                s = 0
                for k in range(j):
                    s += L[i, k] * U[k, j]
                try:
                    L[i, j] = (a[i, j] - s) / U[j, j]
                except RuntimeWarning:
                    raise RuntimeError("Матрица не может быть разложена в LU")
    return L, U


def get_reverse_matrix(a: csr_matrix):
    L, U = get_LU_decomposition(a)
    n = L.shape[0]
    A = csr_matrix(np.zeros((n, n)))
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i < j:
                s = 0
                for k in range(i, n):
                    s += U[i, k] * A[k, j]
                A[i, j] = -(s / U[i, i])
            elif i == j:
                s = 0
                for k in range(j, n):
                    s += U[j, k] * A[k, j]
                A[i, j] = (1 - s) / U[j, j]
            else:
                s = 0
                for k in range(j, n):
                    s += A[i, k] * L[k, j]
                A[i, j] = -s
    return A


if __name__ == "__main__":
    a = generate_random_matrix_sparse(10)
    # ar = get_reverse_matrix(csr_matrix(a))
    # print(check_matrix_equal(ar.todense() * a, np.eye(10)))
    # # L, U = get_LU_decomposition(a)
    # # print(check_matrix_equal(a, L * U))
