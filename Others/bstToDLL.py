# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def join(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        lastLeft = left.left
        lastRight = right.right
        lastLeft.right = right
        right.left = lastLeft
        lastRight.left = left
        left.left = lastRight
        return left

    def treeToDoublyList(self, root):
        if root is None:
            return None
        left = self.treeToDoublyList(root.left)
        right = self.treeToDoublyList(root.right)
        root.left = root
        root.right = root
        return self.join(left, right)
