"""
Given a linked list, determine if it has a cycle in it.

LeetCode Rating: Easy (Const Space is Medium)

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


# constant space soution (this solution was very cool!)
def constSpace(head):
    if head is None or head.next is None:
        return False
    fast = head
    slow = head
    while fast is not None:
        fast = fast.next
        if fast is None:
            return False
        fast = fast.next
        slow = slow.next
        if fast == slow:
            return True
    return False
