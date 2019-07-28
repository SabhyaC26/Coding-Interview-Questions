def fibTD(n, lookup):
    # Base Case
    if n == 0 or n == 1:
        lookup[n] = n

    # if the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fibTD(n-1, lookup) + fibTD(n-2, lookup)

    # return the value corresponding to that value of n
    return lookup[n]


def fibBU(n):

    # array declration
    f = [0]*(n+1)

    # base case
    f[1] = 1

    # driver of the functio
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]


def main():
    n = 20
    lookup = [None] * (101)
    print("Fibonacci number for TD is ", fibTD(n, lookup))
    print("Fibonacci number for BU is ", fibBU(n))


if __name__ == "__main__":
    main()
