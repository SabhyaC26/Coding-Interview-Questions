def fill_water(heights):
    # printing of heights
    r = max(heights)
    c = len(heights)
    outmap = [[' ' for _ in range(c)] for _ in range(r)]
    for i in range(len(heights)):
        for j in range(heights[i]):
            outmap[r-j-1][i] = '+'
    for row in outmap:
        print(''.join(row))


if __name__ == "__main__":
    A = [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3]
    fill_water(A)
