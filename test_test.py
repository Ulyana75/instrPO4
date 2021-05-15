from utilits import *


def test_LU():
    from LU_decomposition import get_LU_decomposition
    n = int(random.random() * 10 + 2)
    A = generate_random_matrix_sparse(n)
    L, U = get_LU_decomposition(A)
    assert check_matrix_equal(A, L * U)


def test_reverse_matrix():
    from LU_decomposition import get_reverse_matrix
    n = int(random.random() * 10 + 2)
    A = generate_random_matrix_sparse(n)
    ar = get_reverse_matrix(csr_matrix(A))
    assert check_matrix_equal(ar.todense() * A, np.eye(n))


def test_SLAU_solving():
    from SLAU import solve
    n = int(random.random() * 10 + 2)
    print(n)
    A = generate_random_matrix_sparse(n)
    b = [random.random() * 100 for _ in range(n)]
    x = solve(csr_matrix(A), csr_matrix(b))
    assert check_SLAU_solution(A.todense(), x.todense(), np.array([b]))
