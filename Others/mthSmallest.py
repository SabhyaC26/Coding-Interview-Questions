# Given k sorted arrays of possibly different sizes, find m-th
# smallest value in the merged array. (m < len(merged))
import heapq


def mthSmallest(lists, m):
    heap = []
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            trip = (lists[i][0], i, 0)
            heapq.heappush(heap, trip)
    merged = []
    while len(heap) > 0:
        elt = heapq.heappop(heap)
        merged.append(elt[0])
        if len(merged) == m-1:
            return merged[-1]
        li = elt[1]
        idx = elt[2]
        if idx < len(lists[li])-1:
            new_trip = (lists[li][idx+1], li, idx+1)
            heapq.heappush(heap, new_trip)
    return 'not found'
