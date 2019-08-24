"""
Given a collection of intervals, merge all overlapping intervals.

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

LeetCode Rating: Medium

Link: https://leetcode.com/problems/merge-intervals/
"""


def getStart(interval):
    return interval[0]


def getEnd(interval):
    return interval[1]


def overlap(A, B):
    # there are 6 ways they be arranged:
    # 1. A fully before B
    if getEnd(A) < getStart(B):
        return False
    # 2. B fully before A
    elif getEnd(A) < getStart(B):
        return False
    # 3. A fully in B
    elif getStart(A) >= getStart(B) and getEnd(A) <= getEnd(B):
        return True
    # 4. B fully in A
    elif getStart(B) >= getStart(A) and getEnd(B) <= getEnd(A):
        return True
    # 5. A before B but overlap
    elif getStart(B) <= getEnd(A):
        return True
    # 6. B before A but overlap
    elif getStart(A) <= getEnd(B):
        return True


def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    # sort the intervals by start time
    sorted_ints = sorted(intervals, key=lambda x: x[0])
    # define stack
    stack = []
    stack.append(sorted_ints[0])
    for pair in sorted_ints[1:]:
        top = stack[-1]
        # if they overlap --> update top's end to end of pair
        if overlap(top, pair):
            top[1] = max(top[1], pair[1])
        # else add pair to the stack
        else:
            stack.append(pair)
    return stack


if __name__ == "__main__":
    print(merge([[1, 3], [15, 18], [2, 6], [8, 10]]))
    print(merge([]))
    print(merge([[1, 3]]))
