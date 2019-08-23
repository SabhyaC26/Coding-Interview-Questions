"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
LeetCode Rating: Easy
Link: https://leetcode.com/problems/climbing-stairs/
"""

# this is a DP approach
def climbStairs(n):
    if n == 1:
        return 1
    M = [0 for x in range(n)]
    M[0], M[1] = 1, 2
    for j in range(2, n):
        M[j] = M[j-1] + M[j-2]
    return M[-1]

if __name__ == "__main__":
    print(climbStairs(10))

