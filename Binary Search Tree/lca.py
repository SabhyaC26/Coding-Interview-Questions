"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    if root == p or root == q:
        return root
    left = right = None
    if root.left:
        left = lowestCommonAncestor(root.left, p, q)
    if root.right:
        right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right
