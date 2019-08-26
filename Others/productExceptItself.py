"""
Given an array nums of n integers where n > 1,  return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

LeetCode Rating: Medium

Link: https://leetcode.com/problems/product-of-array-except-self/
"""


# this is the easy method with division
def easyMethod(arr):
    total = 1
    for elt in arr:
        total *= elt
    return [int(total/elt) for elt in arr]


# now do it without division and in O(n) time
def arrayOfProducts(arr):
    # build the prefix array
    prefixes = []
    prefixes.append(arr[0])
    for num in arr[1:]:
        prefixes.append(prefixes[-1] * num)

    # now build the suffix array
    suffixes = []
    rev = arr
    list.reverse(rev)
    suffixes.append(rev[0])
    for num in arr[1:]:
        suffixes.append(suffixes[-1] * num)
    list.reverse(suffixes)

    # now build the result
    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(suffixes[i+1])
        elif i == len(arr)-1:
            result.append(prefixes[i-1])
        else:
            result.append(prefixes[i-1] * suffixes[i+1])
    return result


if __name__ == "__main__":
    print(arrayOfProducts([1, 2, 3, 4]))
