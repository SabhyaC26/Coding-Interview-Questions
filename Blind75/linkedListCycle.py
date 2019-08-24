"""
Given a linked list, determine if it has a cycle in it.

LeetCode Rating: Easy

Link:
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# linear space solution
def linearSpace(head):
    if head is None or head.next is None:
        return False
    cur = head
    encountered = set([])
    encountered.add(cur)
    while cur is not None:
        cur = cur.next
        if cur in encountered:
            return True
        encountered.add(cur)
    return False


# constant space soution
def constSpace(head):
    pass
