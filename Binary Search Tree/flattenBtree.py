class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def flatten(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None:
        return
    if root.left is not None:
        root.next = root.left
        if root.right is not None:
            root.left.next = root.right
        flatten(root.left)
    elif root.right is not None:
        root.next = root.right
        flatten(root.right)
