def matrix_chain_multiplication(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s


def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")


matrix_dimensions = [10, 30, 5, 60]
m, s = matrix_chain_multiplication(matrix_dimensions)
print("Optimal Parenthesization:")
print_optimal_parenthesization(s, 1, len(matrix_dimensions) - 1)
print("\nMinimum Scalar Multiplications:", m[1][len(matrix_dimensions) - 1])
