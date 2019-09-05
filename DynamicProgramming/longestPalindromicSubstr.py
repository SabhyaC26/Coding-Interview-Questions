# TODO: Given a string, find the longest palindromic substring in a given string.


def longestPalindrome(self, s: str) -> str:
    # 1. create a 2D array, size is len(s) * len(s)
    dp = [[False]*len(s) for _ in range(len(s))]

    # 2. initial lcs related char index
    lcsStartIndex = 0
    lcsEndIndex = 0

    # 3. dp algo
    """
            a b a
            0 1 2
        a 0 T X X
        b 1 F T X
        a 2 T F T
        """
    for i in range(len(s)):
        # what we need is only the left bottom part
        start = i
        end = i
        while start >= 0:
            # case1. if sub-string is 'a'
            if start == end:
                dp[start][end] = True
            # case2. if sub-string is 'ab'
            # We need this case because start + 1 may larger than end - 1 if using case3 directly
            elif start + 1 == end:
                dp[start][end] = s[start] == s[end]
            # case3. if sub-string is 'aba' 'abac' ..etc, i.e. len(sub) >= 3
            else:
                dp[start][end] = dp[start+1][end-1] and (s[start] == s[end])
            # if dp[start][end] is palidromic, check is it longer than current solution
            if dp[start][end] and (end - start + 1) > (lcsEndIndex - lcsStartIndex + 1):
                lcsStartIndex = start
                lcsEndIndex = end
            start = start - 1
    return s[lcsStartIndex:lcsEndIndex+1]
