"""
Invert a binary tree.

LeetCode Rating: Easy

Link: https://leetcode.com/problems/invert-binary-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.right = left
        root.left = right
        return root
