"""
check if a given tree is a BST
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive way
def isBST(root):
    def helper(node, left=float('-inf'), right=float('inf')):
        if not node:
            return True

        val = root.val
        if val <= left or val >= right:
            return False

        if not helper(node.right, val, right):
            return False
        if not helper(node.left, val, left):
            return False
        return True


# iterative DFS method
def isBSTDFS(root):
    if root is None:
        return True

    stack = [(root, float('-inf'), float('inf'))]
    while stack:
        root, lower, upper = stack.pop()
        if not root:
            continue
        val = root.val
        if val <= lower or val >= upper:
            return False
        stack.append((root.right, val, upper))
        stack.append((root.left, lower, val))
    return True
