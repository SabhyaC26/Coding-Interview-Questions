class Solution:
    def helper(self, arr, l, h, key):
        if l > h:
            return -1
        mid = (l + h) // 2
        if arr[mid] == key:
            return mid
        # If arr[l...mid] is sorted
        if arr[l] <= arr[mid]:
            # As this subarray is sorted, we can quickly
            # check if key lies in half or other half
            if key >= arr[l] and key <= arr[mid]:
                return self.helper(arr, l, mid-1, key)
            return self.helper(arr, mid+1, h, key)
        # If arr[l..mid] is not sorted, then arr[mid... r]
        # must be sorted
        if key >= arr[mid] and key <= arr[h]:
            return self.helper(arr, mid+1, h, key)
        return self.helper(arr, l, mid-1, key)

    def search(self, nums: List[int], target: int) -> int:
        h = len(nums)-1
        return self.helper(nums, 0, h, target)
