"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    if (p.val < root.val and root.val < q.val) or (q.val < root.val and root.val < p.val):
        return root
    if (p.val < root.val) and (q.val < root.val):
        return lowestCommonAncestor(root.left, p, q)
    if (p.val > root.val) and (q.val > root.val):
        return lowestCommonAncestor(root.right, p, q)
