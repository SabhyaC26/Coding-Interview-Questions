"""
In the House Robber Problem, you are a robber who has
found a block of houses to rob. Each house i has a
non-negative v(i) worth of value inside that you can steal.
However, due to the way the security systems of the houses
are connected, you’ll get caught if you rob two adjacent houses.
What’s the maximum value you can steal from the block?
"""


def getMaxRob(houses):
    if not houses:
        return 0
    if len(houses) <= 2:
        return max(houses)
    numHouses = len(houses)
    OPT = [0 for i in range(numHouses)]
    OPT[0] = houses[0]
    OPT[1] = max(houses[0:2])
    for j in range(2, numHouses):
        OPT[j] = max(houses[j] + OPT[j-2], OPT[j-1])
    return OPT[-1]


if __name__ == "__main__":
    h = [3, 10, 3, 1, 2]
    print(getMaxRob(h))
