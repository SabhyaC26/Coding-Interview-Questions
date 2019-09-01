class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    if root is None:
        return "Null"
    return str(root.val) + ',' + serialize(root.left) + serialize(root.right)
