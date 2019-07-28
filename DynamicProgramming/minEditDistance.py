def editDistance(m, n):

    M = [[0 for x in range(len(n)+1)] for x in range(len(m)+1)]

    for i in range(len(m)+1):
        for j in range(len(n)+1):

            # if the first string is empty
            # insert all chars of second string
            if (i == 0):
                M[i][j] = j

            # if second string is empty
            # remove all chars of second string
            if (j == 0):
                M[i][j] = i

            # if the last chars are the same
            # ignore and recur
            elif (m[i-1] == n[j-1]):
                M[i][j] = M[i-1][j-1]

            else:
                M[i][j] = 1 + min(M[i][j-1],
                                  M[i-1][j],
                                  M[i-1][j-1])
    return M[len(m)][len(n)]


def main():
    print("Min-Edit-Distance:" +
          str(editDistance("AAHIL", "JACKASS")))


if __name__ == "__main__":
    main()
