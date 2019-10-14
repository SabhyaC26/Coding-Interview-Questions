# // Given a MxN matrix where each element can either be 0 or 1.
# We need to find the shortest path between a given source cell to a
# destination cell. The path can only be created out of a cell if its
# value is 1.

# // Sample input:
# // {{1, 1, 1, 1},
# //  {1, 0, 0, 1},
# //  {1, 1, 1, 1}}

# //  {0,0} -> {2, 1}

# // Sample output:
# // 3

from collections import deque


def isValid(grid, x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0:
        return True
    else:
        return False


def minDistance(grid, start, end):
    # empty conditions
    if not start or not end or not grid or not grid[0]:
        return -1
    # validity check
    if not(isValid(grid, start[0], start[1])) or not(isValid(grid, end[0], end[1])):
        return -1
    # trivial
    if start == end:
        return 0
    # breadth first search
    q = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))
    while q:
        x, y, depth = q.popleft()
        if x == end[0] and y == end[1]:
            return depth
        else:
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if isValid(grid, i, j) and (i, j) not in visited:
                    q.append((i, j, depth+1))
                    visited.add((i, j))
    return -1


A = [[1, 0, 1, 1],
     [1, 1, 0, 1],
     [1, 1, 1, 1]]


s = (0, 0)
e = (2, 1)


print(minDistance(A, e, s))
