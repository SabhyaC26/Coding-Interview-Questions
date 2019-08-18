"""
The longest Increasing Subsequence (LIS) problem is to find the
length of the longest subsequence in a given array such that all
elements of the subsequence are sorted in increasing order.
"""


def getLIS(arr):
    M = [1 for x in range(len(arr))]
    for i in range(0, len(arr)):
        j = 0
        while j < i:
            if arr[j] < arr[i]:
                M[i] = max(M[i], M[j] + 1)
            j += 1
    return max(M)


if __name__ == "__main__":
    # answer should be 7 --> -1,0,2,3,4,5,8
    a1 = [3, 4, -1, 0, 6, 2, 3, 4, 5, -2, 8]
    print(getLIS(a1))
