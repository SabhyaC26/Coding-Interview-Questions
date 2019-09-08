import heapq


def kthLargest(nums, k):
    h = []
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heapop()
    return h[0]
