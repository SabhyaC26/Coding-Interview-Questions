"""
Return the longest common subsequence from two given strings.
"""


def lcsDP(str1, str2):
    # DP algo
    m, n = len(str1), len(str2)
    M = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                M[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                M[i][j] = M[i-1][j-1] + 1
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])
    # reconstruction:
    lcs = ''
    x, y = len(str1)-1, len(str2)-1
    while x >= 0 and y >= 0:
        if str1[x] == str2[y]:
            lcs = str1[x] + lcs
            x -= 1
            y -= 1
        elif M[x-1][y] < M[x][y-1]:
            y -= 1
        else:
            x -= 1
    return M[m][n], lcs


def main():
    print("Longest-Common-Subsequence:" +
          str(lcsDP("SABHYA", "SAMBY")))


if __name__ == "__main__":
    main()
