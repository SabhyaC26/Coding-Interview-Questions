class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def desrialize(data):
    def helper(low=float('-inf'), high=float('inf')):
        if not data or data[-1] < low or data[-1] > high:
            return None

        val = data.pop()
        root = TreeNode(val)
        root.right = helper(val, high)
        root.left = helper(low, val)
        return root

    data = [int(x) for x in data.split(' ') if x]
    return helper()
