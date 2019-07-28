"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
This seemingly simple quetion has a caveat to it --> SEE CODE!
"""

"""
The caveat in the code below is the reversal of the list. It might not be immidiately obvios as to why I reversed the list.
This is why: when you iterate while the list is in the reverse order then, you won't miss the elements. Suppose you start 
from the start then, once you remove the element at the second index, the element at the third index will now move to second 
but in your loop you are incrementing to index 3 now, hence the element which got shifted from index 3 to 2 was never read.
See leetcode question #27
"""
def removeElement(nums, val): 
    for k in reversed(nums):
        if k == val:
            nums.remove(k)
    return len(nums)

def main():
    print(removeElement([1,2,3,4,3,5,3,8], 3))

if __name__ == "__main__":
    main()

