"""
Given two dimensional matrix, write an algorithm to find out the snake sequence
which has the maximum length. There could be many snake sequence in the matrix,
you need to return the one with the maximum length. Travel is allowed only in
two directions, either go right OR go down.

What is snake sequence: Snake sequence can be made if number in adjacent right
cell or number in the adjacent down cell is either +1 or -1 from the number in
the current cell.
"""


def getLongestSnake(M):
    pass


if __name__ == "__main__":
    M = [[1, 2, 1, 2], [7, 7, 2, 5], [6, 4, 3, 4], [1, 2, 2, 5]]
    print(getLongestSnake(M))
