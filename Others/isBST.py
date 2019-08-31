"""
check if a given tree is a BST
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBST(root):
    if root is None:
        return True
    elif root.left is None and root.right is None:
        return True
    elif root.left is not None and root.right is not None:
        if root.left <= root.val and root.val <= root.right:
            return isBST(root.left) and isBST(root.right)
    elif root.left is None and root.right is not None:
        if root.right >= root.val:
            return isBST(root.right)
    elif root.right is None and root.left is not None:
        if root.left <= root.val:
            return isBST(root.left)
