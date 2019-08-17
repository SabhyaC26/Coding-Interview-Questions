"""
The Chain Matrix Multiplication Problem asks,
given a sequence of matrices, what is the fewest
number of operations needed to compute the product
of all the matrices? In other words, if we were to
parenthesize the given chain of matrix multiplications
optimally, how many operations would it take to evaluate
that expression?
"""


def matrixChainMult(matrices):
    def cols(i): return matrices[i][1]
    def rows(i): return matrices[i][0]

    n = len(matrices)
    f = {}  # it can be cleaner to use a map instead of 2D array
    for l in range(1, n + 1):
        for i in range(0, n - l + 1):
            if l == 1:  # base case
                f[(i, i)] = 0
                continue
            k = i + l - 1
            f[(i, k)] = min(
                f[(i, j)] +
                f[(j + 1, k)] +
                (rows(i) * cols(j) * cols(k))
                for j in range(i, k)
            )
    return f[(0, n - 1)]


if __name__ == "__main__":
    print(matrixChainMult([(2, 10), (10, 3), (3, 8)]))
