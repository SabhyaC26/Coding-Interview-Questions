"""
Return the closes value in the BST
"""
from queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def closestVal(root, target):
    smallestDif = abs(root.val - target)
    closest = root.val
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node.left is not None:
            q.put(node.left)
            dif = abs(target-node.left.val)
            if dif < smallestDif:
                smallestDif = dif
                closest = node.left.val
        if node.right is not None:
            q.put(node.right)
            dif = abs(target-node.right.val)
            if dif < smallestDif:
                smallestDif = dif
                closest = node.right.val
    return closest
