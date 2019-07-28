def knapSack(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than the Knapsack of capacity
    # W, then this item cannot be in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of the two cases
    # (1) nth item included
    # (2) not included
    else:
        return max((val[n-1] + knapSack(W-wt[n-1], wt, val, n-1)),
                   knapSack(W, wt, val, n-1))


# HOW DO WE DO THIS BOTTOM UP?? YES HOW? YOU TELL ME

def bottomUpKnapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottup up manner
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][w]


def main():

    # test the above code
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print("KS Recursive: " + str(knapSack(W, wt, val, n)))

    print("KS Bottom Up: " + str(bottomUpKnapSack(W, wt, val, n)))


if __name__ == "__main__":
    main()
