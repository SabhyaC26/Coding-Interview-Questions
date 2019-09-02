class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    res = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break
        node = stack.pop()
        res.append(node.val)
        root = node.right
    return res
