def lcsDP(str1, str2):

    m = len(str1)
    n = len(str2)

    M = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):

        for j in range(n+1):

            if i == 0 or j == 0:
                M[i][j] = 0

            elif str1[i-1] == str2[j-1]:
                M[i][j] = M[i-1][j-1] + 1

            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])

    return M[m][n]


def main():
    print("Longest-Common-Subsequence:" +
          str(lcsDP("AGGTAB", "GXTXAYB")))


if __name__ == "__main__":
    main()
