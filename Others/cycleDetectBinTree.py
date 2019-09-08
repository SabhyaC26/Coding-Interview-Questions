class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def detectCycle(self, root, seen):
        if root in seen:
            return True
        seen.add(root)
        if root.left and self.detectCycle(root.left, seen):
            return True
        if root.right and self.detectCycle(root.right, seen):
            return True
        return False
