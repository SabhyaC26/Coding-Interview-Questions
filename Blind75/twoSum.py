"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
LeetCode Link: https://leetcode.com/problems/two-sum/
LeetCode Rating: Easy
"""


def twoSum(nums, target):
    reverseLookup = {}
    for i in range(len(nums)):
        reverseLookup[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in reverseLookup and reverseLookup[complement] != i:
            return [i, reverseLookup[complement]]


def twoSumOnePass(nums, target):
    reverseLookup = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in reverseLookup:
            return [i, reverseLookup[complement]]
        reverseLookup[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 13
    print(twoSum(nums, target))
    print(twoSumOnePass(nums, target))
