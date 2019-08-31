"""
check if a given tree is a BST
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive way - I don't like this very much
def isBST(root):
    def helper(node, left=float('inf'), right=float('inf')):
        if not node:
            return True

        val = root.val
        if val <= left or val >= right:
            return False

        if not helper(node.right, val, right):
            return False
        if not helper(node.left, val, left):
            return False
        return True
