import heapq
"""
Find the kth largest element in an array
"""


# simple sort approach
def findKthLargestSort(nums, k):
    nums.sort(reversed=True)
    return nums[k-1]


# heap approach
def findKthLargestHeap(nums, k):
    h = []
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]


# quickselect approach
