from utilits import *


def test_LU_decomposition(quantity_of_test: int):
    from LU_decomposition import get_LU_decomposition
    for _ in range(quantity_of_test):
        n = int(random.random() * 10 + 1)
        A = generate_random_matrix_sparse(n)
        try:
            L, U = get_LU_decomposition(A)
        except RuntimeError:
            quantity_of_test += 1
            continue
        result = check_matrix_equal(A, L * U)
        print("result:", result)
        if not result:
            print("matrix, which broke:")
            print(A, '\n')
        else:
            print("matrix, which is fine:")
            print(A, '\n')


def test_get_reverse_matrix(quantity_of_test: int):
    from LU_decomposition import get_reverse_matrix
    for _ in range(quantity_of_test):
        n = int(random.random() * 10 + 2)
        A = generate_random_matrix_sparse(n)
        try:
            ar = get_reverse_matrix(csr_matrix(A))
        except RuntimeError:
            quantity_of_test += 1
            continue
        except:
            print("Exception was thrown")
            print("matrix, which broke:")
            print(A, '\n')
            continue
        result = check_matrix_equal(ar.todense() * A, np.eye(n))
        print("result:", result)
        if not result:
            print("matrix, which broke:")
            print(A, '\n')
        else:
            print("matrix, which is fine:")
            print(A, '\n')


def test_SLAU_solving(quantity_of_test: int):
    from SLAU import solve
    for _ in range(quantity_of_test):
        n = int(random.random() * 10 + 1)
        print(n)
        A = generate_random_matrix_sparse(n)
        b = [random.random() * 100 for _ in range(n)]
        try:
            x = solve(csr_matrix(A), csr_matrix(b))
        except RuntimeError:
            quantity_of_test += 1
            continue
        result = check_SLAU_solution(A.todense(), x.todense(), np.array([b]))
        print("result:", result)
        if not result:
            print("matrix, which broke:")
            print("A:")
            print(A, '\n')
            print("b:")
            print(b, '\n')
        else:
            print("matrix, which is fine:")
            print(A, '\n')
            print("b:")
            print(b, '\n')


def test_seidel_method(quantity_of_test: int):
    from seidel_method import solve
    for _ in range(quantity_of_test):
        n = int(random.random() * 10 + 1)
        print(n)
        A = generate_random_matrix_sparse(n)
        b = [random.random() * 100 for _ in range(n)]
        try:
            x = solve(csr_matrix(A), csr_matrix(b))
        except RuntimeError:
            quantity_of_test += 1
            continue
        result = check_SLAU_solution(csr_matrix(A), csr_matrix(x), csr_matrix(b))
        print("result:", result)
        if not result:
            print("matrix, which broke:")
            print("A:")
            print(A, '\n')
            print("b:")
            print(b, '\n')
        else:
            print("matrix, which is fine:")
            print(A, '\n')
            print("b:")
            print(b, '\n')


if __name__ == "__main__":
    test_LU_decomposition(10)
    test_get_reverse_matrix(10)
    test_SLAU_solving(10)
    test_seidel_method(10)
