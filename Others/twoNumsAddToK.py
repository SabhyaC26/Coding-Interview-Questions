"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

def getPair(nums, target):
    complements = {}
    for val in nums:
        if val in complements.values():
            return (val, target-val)
        complements[val] = target - val
    return (0,0)


def main():
    nums = [10, 15, 3, 7]
    t = 17
    print(getPair(nums, t))

if __name__ == "__main__":
    main()
