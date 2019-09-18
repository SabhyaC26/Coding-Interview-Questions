class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def seperateOddEvens(head):
    cur = head
    while cur.next is not None:
        cur = cur.next
    tail = cur
    newCur = head
    while newCur != tail:
        if newCur.val % 2 != 0:
            tail.next = newCur
            tail = tail.next
    return cur
