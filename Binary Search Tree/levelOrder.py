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
    q = Queue()
    q.put(root)

    while q:
        node = q.get()
        print(node.val)
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)
