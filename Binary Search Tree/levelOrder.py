from queue import Queue

"""
Do a level order traversal of a Binary Tree
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# for level order you have to use BFS
def levelOrder(root):
    if root is None:
        return []

    q = Queue()
    q.put(root)
    dmap = {}
    dmap[root] = 1
    maxd = 1

    while not q.empty():
        node = q.get()
        if node.left is not None:
            q.put(node.left)
            dmap[node.left] = 0
            dmap[node.left] = dmap[node] + 1
            if dmap[node.left] > maxd:
                maxd += 1
        if node.right is not None:
            q.put(node.right)
            dmap[node.right] = 0
            dmap[node.right] = dmap[node] + 1
            if dmap[node.right] > maxd:
                maxd += 1
    bigList = []
    for d in range(1, maxd+1):
        dlist = []
        for key, value in dmap.items():
            if value == d:
                dlist.append(key.val)
        bigList.append(dlist)
    return bigList
