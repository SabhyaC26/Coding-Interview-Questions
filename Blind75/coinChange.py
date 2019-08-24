"""
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

LeetCode Rating: Medium

Link: https://leetcode.com/problems/coin-change/
"""


# DP SOLUTION
def coinChange(coins, amount):
    M = [(amount+1) for i in range(amount+1)]
    M[0] = 0
    for j in range(amount+1):
        for c in coins:
            if c <= j:
                if M[j-c] + 1 < M[j]:
                    M[j] = M[j-c] + 1
    return M[amount] if M[amount] <= amount else -1
