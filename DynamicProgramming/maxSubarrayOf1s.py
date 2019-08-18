"""
Given a matrix of 0’s and 1’s (binary matrix).
Find out Maximum size square sub-matrix with all 1’s.
"""


def getOnesSubMtxDim(M):
    # returnd the diemnsion of the sub matrix
    cols = len(M[0])
    rows = len(M)
    OPT = [[0 for x in range(0, cols)] for x in range(0, rows)]
    for x in range(0, cols):
        OPT[0][x] = M[0][x]
    for x in range(0, rows):
        OPT[x][0] = M[x][0]
    for i in range(1, rows):
        for j in range(1, cols):
            OPT[i][j] = min(OPT[i-1][j], OPT[i][j-1], OPT[i-1][j-1]) + 1
    return max(max(OPT))


if __name__ == "__main__":
    matrix = [
        [0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1]
    ]

    print(getOnesSubMtxDim(matrix))
