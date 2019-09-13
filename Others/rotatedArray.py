# search roated array
def searchRotated(arr, lo, hi, key):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == key:
        return mid
    # arr[lo...mid] is sorted
    if arr[lo] <= arr[mid]:
        # now check if key is in this sorted portion or not
        if key >= arr[lo] and key <= arr[mid]:
            return searchRotated(arr, lo, mid-1, key)
        else:
            return searchRotated(arr, mid+1, hi, key)
    # if arr[lo...mid] is not sorted, then arr[mid...r] must be sorted
    else:
        if key >= arr[mid] and key <= arr[hi]:
            return searchRotated(arr, mid+1, hi, key)
        else:
            return searchRotated(arr, lo, mid-1, key)


def caller(arr, key):
    return searchRotated(arr, 0, len(arr)-1, key)
