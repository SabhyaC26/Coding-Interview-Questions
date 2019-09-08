"""
return the kth largest with dups
"""
import heapq


def kthLargestDups(nums, k):
    nums = set(nums)
    if len(nums) < k:
        return max(nums)
    h = []
    for _ in range(k):
        heapq.heappush(h, nums.pop())
    while nums:
        heapq.heappushpop(h, nums.pop())
    return h[0]
