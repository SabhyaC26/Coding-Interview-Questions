"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
"""
import math


def binToDec(a):
    maxPo = len(a)-1
    dec = 0
    for c in a:
        if int(c) == 1:
            dec += 2 ** maxPo
        maxPo -= 1
    return dec


def decToBin(a):
    if(a > 1):
        decToBin(a//2)
    print(a % 2)


if __name__ == "__main__":
    print(binToDec("101"))
    print(decToBin(100))
