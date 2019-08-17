# make change - arbitrary input for coin denominations

american = [1, 5, 10, 25, 50, 100]


def greedyChange(cents):
    num_coins = 0
    while cents > 0:
        if cents >= 100:
            cents -= 100
            num_coins += 1
        else:
            for i in range(len(american)):
                if american[i] <= cents and american[i+1] > cents:
                    cents -= american[i]
                    num_coins += 1
    return num_coins


# now for arbitrary coin denominations
def makeChangeDP(n, coins):
    M = [(n+1) for i in range(n+1)]
    M[0] = 0
    for j in range(n+1):
        for c in coins:
            if c <= j:
                if M[j-c] + 1 < M[j]:
                    M[j] = M[j-c] + 1
    return M[n] if M[n] <= n else None


if __name__ == "__main__":
    print(greedyChange(200))
    print(makeChangeDP(11, [1, 2, 5]))
