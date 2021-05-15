import random
import numpy as np
from scipy.sparse import csr_matrix


def generate_random_matrix_sparse(n):
    A = csr_matrix(np.zeros((n, n)))
    non_empty = int(random.uniform(0.7, 1) * (n ** 2))
    indexes = []
    for i in range(n):
        for j in range(n):
            indexes.append((i, j))
    l = len(indexes)
    for i in range(non_empty):
        index = int(random.random() * l)
        ind_1, ind_2 = indexes[index]
        A[ind_1, ind_2] = random.random() * 10
        del indexes[index]
        l -= 1
    return A


def generate_random_matrix_close(n):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i][j] = random.random() * 100 + 1
    return A


def check_matrix_equal(a, b):
    eps = 0.0000001
    n = a.shape[0]
    for i in range(n):
        for j in range(n):
            if abs(a[i, j] - b[i, j]) > eps:
                return False
    return True


def check_SLAU_solution(a: np.array, x: np.array, b: np.array):
    b2 = a.dot(x.T)
    return check_matrix_equal(b, b2)
