"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.

LeetCode Rating: Easy (Super Easy in fact)
Link: https://leetcode.com/problems/contains-duplicate/
"""


def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
