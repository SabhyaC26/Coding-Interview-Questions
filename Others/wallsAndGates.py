from collections import deque


def wallsAndGates(rooms):
    if not rooms:
        return
    r, c = len(rooms), len(rooms[0])
    for i in range(r):
        for j in range(c):
            if rooms[i][j] == 0:
                q = deque([])
                q.append((i+1, j, 1))
                q.append((i-1, j, 1))
                q.append((i, j+1, 1))
                q.append((i, j-1, 1))
                visited = set()
                while q:
                    x, y, val = q.popleft()
                    if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] in [0, -1] or (x, y) in visited:
                        continue
                    visited.add((x, y))
                    rooms[x][y] = min(rooms[x][y], val)
                    q.append((x+1, y, val+1))
                    q.append((x-1, y, val+1))
                    q.append((x, y+1, val+1))
                    q.append((x, y-1, val+1))
