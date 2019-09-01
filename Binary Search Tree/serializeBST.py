class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    def post(root):
        return post(root.left) + post(root.right) + [root.val] if root else []
    return ' '.join(map(str, post(root)))
