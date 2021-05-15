import numpy as np

from utilits import *
from math import sqrt


def check_stop(x, y, eps=0.0001):
    n = x.shape[0]
    s = 0
    for i in range(n):
        s += (x[i] - y[i]) ** 2
    return sqrt(s) < eps


def solve(a, b):
    n = a.shape[0]
    xk = np.zeros(n)

    n_max = 1000

    for _ in range(n_max):
        xk1 = xk.copy()

        for i in range(n):
            s1 = 0
            for j in range(i):
                c = -a[i, j] / a[i, i]
                s1 += c * xk1[j]

            s2 = 0
            for j in range(i + 1, n):
                c = -a[i, j] / a[i, i]
                s2 += c * xk[j]

            d = b[0, i] / a[i, i]
            xk1[i] = s1 + s2 + d

        if check_stop(xk, xk1):
            break

        xk = xk1.copy()
    return xk


if __name__ == "__main__":
    a = generate_random_matrix_sparse(3)
    b = [random.random() * 100 for i in range(3)]
    x = solve(csr_matrix(a), csr_matrix(b))
    print(check_SLAU_solution(csr_matrix(a), csr_matrix(x), csr_matrix(b)))
