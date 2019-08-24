"""
Given an array nums of n integers, are there elements a, b, c in nums such
that a + b + c = 0? Find all unique triplets in the array which gives the
sum of zero.
LeetCode Rating: Medium
Link: https://leetcode.com/problems/3sum/
"""


# TODO
def threeSumImproved(nums):
    pass


# this is horrible code! - very poor time complexity
# i will improve this
def threeSum(nums):
    if len(nums) < 3:
        return []
    # everytime you add a triplet to the set just sort it
    solutionSet = []
    # init the two pointers
    rev_ij_lookup = {}
    for i in range(len(nums)):
        for j in range(len(nums)):
            keys = list(rev_ij_lookup.keys())
            key_set = [(k[0], k[1]) for k in keys]
            if i != j and (i, j) not in key_set and (j, i) not in key_set:
                target = -(nums[i] + nums[j])
                rev_ij_lookup[(i, j, nums[i], nums[j])] = target
    # now for each key in the rev lookup check if it is there in the array
    for key in rev_ij_lookup.keys():
        for k in range(len(nums)):
            i = key[0]
            j = key[1]
            i_val = key[2]
            j_val = key[3]
            if k != i and k != j and nums[k] == rev_ij_lookup[key]:
                trip_arr = [i_val, j_val, rev_ij_lookup[key]]
                trip_arr.sort()
                trip = tuple(trip_arr)
                print(trip)
                if trip not in solutionSet:
                    solutionSet.append(trip)
    return [list(tup) for tup in solutionSet]


if __name__ == "__main__":
    A = [3, 0, -2, -1, 1, 2]
    print(threeSum(A))
