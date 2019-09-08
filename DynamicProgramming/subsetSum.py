def subsetSum(arr, k):
    # num rows in DP table
    rows = len(arr)
    # num cols in DP table
    cols = k
    # initialize the DP table
    DP = [[False for _ in range(cols+1)] for _ in range(rows)]
    # everything in the first col of DP will be true
    # as the target sum of 0 is always satisfied
    for x in range(rows):
        DP[x][0] = True
    # let's also fill up the first row --> the case where have just one day's food to consider
    for x in range(cols):
        if x == arr[0]:
            DP[0][x] = True

    # we can now start populating the DP table (O(N^2) algorithm)
    for i in range(1, rows):
        for j in range(cols+1):
            if j < arr[i]:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i-1][j] or DP[i-1][j-arr[i]]

    print(DP)

    # after the DP table is full, we can return the bottom right corner
    return DP[-1][-1]


if __name__ == "__main__":
    print(subsetSum([2, 3, 7, 8, 10], 11))
