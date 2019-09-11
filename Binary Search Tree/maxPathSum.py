class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            # max sum on the left and right sub trees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            # price to start a new path where node is the highest
            price_newpath = node.val + left_gain + right_gain
            # update the max_sum if its better
            max_sum = max(max_sum, price_newpath)
            # lastly
            return node.val + max(left_gain, right_gain)
        max_sum = float('-inf')
        max_gain(root)
        return max_sum
