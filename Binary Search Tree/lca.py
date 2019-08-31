"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root.val == val:
        return True
    if root and val < root.val:
        return searchBST(root.left, val)
    if root and val > root.val:
        return searchBST(root.right, val)
    return False


def lowestCommonAncestor(root, p, q):
    if root == p or root == q:
        return root
    # cases --> p in left and q in right OR p in right and q in left
    if searchBST(root.left, p.val) and searchBST(root.right, q.val):
        return root.val
    elif searchBST(root.right, p.val) and searchBST(root.left, q.val):
        return root.val
    # check if both are in left
    elif searchBST(root.left, p.val) and searchBST(root.right. q.val):
        return lowestCommonAncestor(root.left, p, q)
    # check if both are in right
    elif searchBST(root.right, p.val) and searchBST(root.right. q.val):
        return lowestCommonAncestor(root.right, p, q)
