class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def searchBST(root: TreeNode, val: int) -> TreeNode:
    if root and val < root.val:
        return searchBST(root.left, val)
    if root and val > root.val:
        return searchBST(root.right, val)
    return root
