"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the binary search tree.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
        # If both p and q are greater than parent
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    # If both p and q are lesser than parent
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    # We have found the split point, i.e. the LCA node.
    else:
        return root
