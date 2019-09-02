class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    stack = []
    res = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return
        node = stack.pop()
        res.append(node)
        if len(res) >= 2 and res[-2] == p:
            return res[-1]
        root = node.right
