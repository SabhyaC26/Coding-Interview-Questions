class Solution(object):
    def __init__(self, arr):
        prefixSum = [0 for _ in range(len(arr))]
        prefixSum[0] = 0
        for i in range(1, len(arr)):
            if arr[i-1] == 1:
                prefixSum[i] = prefixSum[i-1] + 1
            else:
                prefixSum[i] = prefixSum[i-1]
        self.preSums = prefixSum

    def howManyOnes(self, start, end):
        return self.preSums[end] - self.preSums[start]


if __name__ == "__main__":
    arr = [0, 1, 1, 1, 0, 0]
    first = Solution(arr)
    print(first.howManyOnes(0, 3))
