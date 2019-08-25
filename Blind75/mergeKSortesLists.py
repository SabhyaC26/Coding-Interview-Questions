from queue import PriorityQueue
"""
Merge K Sorted Lists

LeetCode Rating: Hard
"""


# START EASY --> MERGE TWO SORTED LISTS (O(N) algo)
def mergeTwoLists(l1, l2):
    # if either list if empty
    if not l1:
        return l2
    if not l2:
        return l1
    # define the pointers
    p1 = 0
    p2 = 0
    # define the merged list
    merged = []
    while p1 <= len(l1)-1 and p2 <= len(l2)-1:
        if l1[p1] < l2[p2]:
            merged.append(l1[p1])
            p1 += 1
        else:
            merged.append(l2[p2])
            p2 += 1
    # this means l1 finished before so add the rest of l2 to merged
    if not p1 <= len(l1)-1:
        merged += l2[p2:]
    # vice verse
    else:
        merged += l1[p1:]
    return merged


# THEN HARD --> MERGE K SORETD LISTS (using heaps)
def mergeKLists(lists):
    # remove all empty lists --> to prevent errors
    for l in lists:
        if l == []:
            lists.remove(l)
    # now build the heap
    heap = PriorityQueue()
    for i in range(len(lists)):
        # trip[0] is the actual elt
        # trip[1] is the index of the list in lists
        # trip[2] is the index of the element in the list
        trip = (lists[i][0], i, 0)
        heap.put(trip)
    # define merged list
    merged = []
    while heap.qsize() > 0:
        elt = heap.get()
        merged.append(elt[0])
        li = elt[1]
        idx = elt[2]
        # if we have not reached the end of the list
        if idx < len(lists[li])-1:
            trip = (lists[li][idx+1], li, idx+1)
            heap.put(trip)
    return merged


if __name__ == "__main__":
    A = [1, 3, 5, 7]
    B = [2, 4, 6, 8, 10, 12]
    C = [3, 4, 8, 10, 13, 29, 32]
    D = [14, 15, 17, 18, 24, 30]
    print(mergeTwoLists(A, B))
    print(mergeKLists([A, B, C, D]))
