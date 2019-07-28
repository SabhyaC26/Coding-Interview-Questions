def climbStairs(n):
    if n == 1:
        return 1
    DP = [0 for x in range(n)]
    DP[0], DP[1] = 1, 2
    for j in range(2, n):
        DP[j] = DP[j-1] + DP[j-2]
    return DP[-1]
        
def main():
    print(climbStairs(3))
    print(climbStairs(20))

if __name__ == "__main__":
    main()
