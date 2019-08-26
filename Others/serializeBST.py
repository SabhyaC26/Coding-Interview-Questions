class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    if root is None:
        return "Null"
    else:
        serialize(root.left)
        print(root.val)
        serialize(root.right)
