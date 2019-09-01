from queue import Queue
"""
Return the min depth of a Binary Tree
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0

    q = Queue()
    q.put(root)
    dmap = {}
    dmap[root] = 1
    depths = []

    while not q.empty():
        node = q.get()
        # check if leaf node
        if node.left is None and node.right is None:
            depths.append(dmap[node])
        if node.left is not None:
            q.put(node.left)
            dmap[node.left] = 0
            dmap[node.left] = dmap[node] + 1
        if node.right is not None:
            q.put(node.right)
            dmap[node.right] = 0
            dmap[node.right] = dmap[node] + 1
    return min(depths)
