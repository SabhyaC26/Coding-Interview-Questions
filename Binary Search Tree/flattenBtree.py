class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def __init__(self):
    self.prev = None


def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None:
        return None
    self.flatten(root.right)
    self.flatten(root.left)
    root.right = self.prev
    root.left = None
    self.prev = root
