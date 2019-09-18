def leftmostoneindex(matrix):
    rows = len(matrix)
    cols = len(matrix)
    candidate = -1
    r = 0
    c = cols - 1
    while r < rows and c >= 0:
        if matrix[r][c] == 1:
            candidate = c
            c -= 1
        else:
            r += 1
    return candidate


if __name__ == "__main__":
    matrix = [[1, 1, 1, 1],
              [0, 0, 1, 1],
              [0, 1, 1, 1],
              [0, 0, 0, 0]]
    print(leftmostoneindex(matrix))
