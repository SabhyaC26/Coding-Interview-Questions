"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
The robot can only move in two directions, right and down, but certain cells are "off limits" such 
that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left 
to the bottom right.
"""

# this is a recursive solution that is not efficient
def countPaths(grid, row, col):
    if row >= len(grid):
        return 0
    if col >= len(grid[0]):
        return 0
    # if the square is not valid --> return 0
    if grid[row][col] == 1:
        return 0
    # if you reach the end (represented by -1) return 1
    if grid[row][col] == -1:
        return 1
    return countPaths(grid, row+1, col) + countPaths(grid, row, col+1)
    
# this a dynamic programming approach that is space and time efficient
def countPathsDP(grid):
    M = [[0 for x in range(len(grid[0]))] for x in range(len(grid))]
    # still to complete (might change some representations)

def main():
    g1 = [[0, 0, 0, 0],
          [0, 0, 0, 0], 
          [0, 0, 0, 0],
          [0, 0, 0, -1]]
    print(countPaths(g1, 0, 0))
    print(countPathsDP(g1))

if __name__ == "__main__":
    main()
    
