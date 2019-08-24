"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security
system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.

LeetCode Rating: Easy (recursive is Easy, DP is medium in my opinion)

I've done this before, but no harm in doing it again.
"""

# this is the DP approach - recursive is very trivial


def rob(nums):
    # do you rob the jth house -> yes or no
    # so choose max between val(j) + opt[j-2] or opt[j-1]
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    numHouses = len(nums)
    OPT = [0 for i in range(numHouses)]
    OPT[0] = nums[0]
    OPT[1] = max(nums[0:2])
    for j in range(2, numHouses):
        OPT[j] = max(nums[j] + OPT[j-2], OPT[j-1])
    return OPT[-1]
