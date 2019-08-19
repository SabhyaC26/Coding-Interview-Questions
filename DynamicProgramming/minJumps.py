"""
Given an array of non negative integers, start from the first element and reach
the last by jumping. The jump length can be at most the value at the current
position in the array. Optimum result is when you reach the goal in minimum
number of jumps.
"""


def minJumpsRec(arr, startIndex, endIndex):
    # Base Cases
    if startIndex == endIndex:
        return 0
    if arr[startIndex] == 0:
        return float('inf')

    # Now traverse through all the points reachable from arr[startIndex].
    # Recursively get the minimum number of jumps needed to reach arr[endIndex]
    # from these reachable points.
    minJs = float('inf')
    for i in range(startIndex+1, endIndex+1):
        if (i < startIndex + arr[startIndex] + 1):
            jumps = minJumpsRec(arr, i, endIndex)
            if (jumps + 1 < minJs):
                minJs = jumps + 1
    return minJs


def minJumpsDP(arr):
    if arr[0] == 0:
        return float('inf')
    startIndex = 0
    endIndex = len(arr)-1
    OPT = [0 for i in range(endIndex+1)]
    for i in range(1, endIndex+1):
        OPT[i] = float('inf')
        for j in range(0, i):
            if i <= j + arr[j] and OPT[j] != float('inf'):
                OPT[i] = min(OPT[i], OPT[j] + 1)
    return OPT[-1]


if __name__ == "__main__":
    A = [2, 3, 1, 1, 4, 1, 1, 4, 4, 2, 5, 2, 5, 2]
    print(minJumpsRec(A, 0, len(A)-1))
    print(minJumpsDP(A))
