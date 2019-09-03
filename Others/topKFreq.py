"""
Given a non-empty array of integers, return the k most frequent elements.
"""
import heapq


# using hahsmaps and heap
def topKFreq(nums, k):
    freq = {}
    h = []
    for num in nums:
        if num in freq.keys():
            freq[num] += 1
        else:
            freq[num] = 1
    for key, val in freq.items():
        heapq.heappush(h, (val, key))
        if len(h) > k:
            heapq.heappop(h)
    return [m[1] for m in h]
