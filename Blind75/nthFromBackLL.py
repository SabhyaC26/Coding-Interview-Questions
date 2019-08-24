"""
Given a linked list, remove the n-th node from the end of list
and return its head.

LeetCode Rating: Medium

Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# this is pretty easy
def twoPass(head, n):
    if head.next is None:
        return None
    if head.next.next is None:
        if n == 1:
            head.next = None
            return head
        if n == 2:
            return head.next
    cur = head
    # first pass through the list to get the length
    length = 0
    while cur is not None:
        cur = cur.next
        length += 1
    # now nth from back is len-n from front
    target = length - n
    if target == 0:
        return head.next
    cur = head
    for i in range(target-1):
        cur = cur.next
    cur.next = cur.next.next
    return head


# this is when things get fun!


def onePass():
    pass
