"""
You are given a rod of size n>0, it can be cut into any number of pieces k
(k ≤ n). Price for each piece of size i is represented as p(i) and maximum
revenue from a rod of size i is r(i) (could be split into multiple pieces).
Find r(n) for the rod of size n.
"""


def cutRodRecursive(n, prices):
    if n <= 0:
        return 0
    max_val = 0
    for i in range(0, n):
        max_val = max(max_val, prices[i] + cutRodRecursive(n-i-1, prices))
    return max_val


def cutRodDP(n, prices):
    M = {}
    M[0] = 0
    for j in range(1, n+1):
        M[j] = max([prices[i] + M[j-i] for i in range(1, j+1)])
    return M[n]


if __name__ == "__main__":

    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(cutRodRecursive(4, prices))

    pricesDict = {
        1: 1,
        2: 5,
        3: 8,
        4: 9,
        5: 10,
        6: 17,
        7: 17,
        8: 20,
        9: 24,
        10: 30
    }
    print(cutRodDP(4, pricesDict))
