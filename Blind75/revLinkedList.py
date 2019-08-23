"""
Reverse a singly linked list.
Link: https://leetcode.com/problems/reverse-linked-list/
LeetCode Rating: Easy

Followup: A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


# iteravtive version
def revLinkedListIter(head):
    if head.next is None:
        return head
    current = head
    stack = []
    while current is not None:
        stack.append(current.val)
        current = current.next
    newHead = ListNode(stack[-1])
    stack.pop()
    cur = newHead
    while stack:
        cur.next = ListNode(stack.pop())
        cur = cur.next
    return newHead


# recursive version
def revLinkedListRec(head):
    if head is None or head.next is None:
        return head
    p = revLinkedListRec(head.next)
    head.next.next = head
    head.next = None
    return p


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print(revLinkedListIter(node1))
    print(revLinkedListRec(node1))
