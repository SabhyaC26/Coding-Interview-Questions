"""
Given a complete binary tree, count the number of nodes.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # easy way in linear time
    def countNodes(self, root):
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0

    # tricky way using bin search
