from collections import deque
"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.
LeetCode Rating: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# tree definition
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# returns the max depth recursively
def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# returns the max depth iteratively
def maxDepthIter(root):
    if root is None:
        return 0
    nodeQ = deque()
    depthMap = {}
    nodeQ.append(root)
    depthMap[root] = 0
    while nodeQ:
        cur = nodeQ.popleft()
        if cur.left is not None:
            nodeQ.append(cur.left)
            depthMap[cur.left] = depthMap[cur] + 1
        if cur.right is not None:
            nodeQ.append(cur.right)
            depthMap[cur.right] = depthMap[cur] + 1
    # now find the max in depth map
    return max([val for val in depthMap.values()])
