class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterative DFS method
def bstPaths(root):
    if root is None:
        return []
    paths = []
    stack = []
    stack.append((root, str(root.val)))
    while stack is not None:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.left:
            stack.append((node.left, path + '->' + str(node.left.val)))
        if root.right:
            stack.append((node.right, path + '->' + str(node.right.val)))
