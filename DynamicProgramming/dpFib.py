def fibTopDown(n, lookup):
    # Base Case
    if n == 0 or n == 1:
        lookup[n] = n

    # if the value is not calculated then do it
    if lookup[n] is None:
        lookup[n] = fibTopDown(n-1, lookup) + fibTopDown(n-2, lookup)

    # return the corresponding value if n is calculated already
    return lookup[n]


def fibBotUp(n):
    M = [0 for i in range(n+1)]
    M[1] = 1
    for i in range(2, n+1):
        M[i] = M[i-1] + M[i-2]
    return M[i]


def main():
    n = 20
    lookup = [None for i in range(101)]
    print("Fibonacci number for TD is ", fibTopDown(n, lookup))
    print("Fibonacci number for BU is ", fibBotUp(n))


if __name__ == "__main__":
    main()
