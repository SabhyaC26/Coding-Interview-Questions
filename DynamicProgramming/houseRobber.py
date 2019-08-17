"""
In the House Robber Problem, you are a robber who has
found a block of houses to rob. Each house i has a
non-negative v(i) worth of value inside that you can steal.
However, due to the way the security systems of the houses
are connected, you’ll get caught if you rob two adjacent houses.
What’s the maximum value you can steal from the block?
"""


def getMaxRob(houses):
    n = len(houses)
    M = [0 for i in range(n)]
    M[0] = houses[0]
    M[1] = houses[1]
    for j in range(2, n):
        M[j] = max(houses[j] + M[j-2], M[j-1])
    return M[n-1]


if __name__ == "__main__":
    h = [3, 10, 3, 1, 2]
    print(getMaxRob(h))
