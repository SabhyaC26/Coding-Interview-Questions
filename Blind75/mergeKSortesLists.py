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


if __name__ == "__main__":
    A = [1, 3, 5, 7]
    B = [2, 4, 6, 8, 10, 12]
    print(mergeTwoLists(A, B))
