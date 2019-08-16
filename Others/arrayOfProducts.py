"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# simple solution - multiply all and then divide by the num at that index
def easySol(arr):
    total = 1
    for elt in arr:
        total = total * elt
    for i in range(len(arr)):
        val = arr[i]
        arr[i] = int(total/val)
    return arr

# follow up - can't use division
def hardSol(arr):
    pass

def main():
    arr = [1, 2, 3, 4, 5]
    print(easySol(arr))

if __name__ == "__main__":
    main()
