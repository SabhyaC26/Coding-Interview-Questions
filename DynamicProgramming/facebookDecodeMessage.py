from collections import defaultdict
"""
a --> 1
b --> 2
...
z --> 26

eg. "12" --> "ab" or "l" so numWays(12) --> 2
"""

# returns the number of ways we can decode data[k:]


def helper(data, k):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == '0':
        return 0

    result = helper(data, k-1)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper(data, k-2)
    return result


def recNumWays(data):
    return helper(data, len(data))


def numWaysDP(s):
    # todo


if __name__ == "__main__":
    print(recNumWays("12"))
