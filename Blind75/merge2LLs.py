"""
Merge two sorted linked lists and return it as a new list. The new list
should be made by splicing together the nodes of the first two lists.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    if l2 is None:
        return l1
    if l1 is None:
        return l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
