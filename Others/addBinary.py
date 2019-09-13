"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
"""
import math


def addBinary(a, b):
    result = ''
    carry = 0
    a = list(a)
    b = list(b)
    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        result = str(carry % 2) + result
        carry = carry // 2
    return result
