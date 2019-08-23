"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
LeetCode Link: https://leetcode.com/problems/two-sum/
LeetCode Rating: Easy
"""


def twoSum(nums, target):
    complements = {}
    for i in range(len(nums)):
        complements[nums[i]] = i
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in complements and complements[comp] != i:
            return [i, complements[comp]]


# TODO
def twoSumOnePass(nums, target):
    pass


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 10
    print(twoSum(nums, target))
