def subsetSum(arr, k):
    i = len(arr)
    j = k
    # initialize the DP table
    DP = [[False for _ in range(j+1)] for _ in range(i)]
    # everything in the first col of DP will be true
    # as the target sum of 0 is always satisfied
