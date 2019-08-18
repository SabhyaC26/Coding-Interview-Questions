# find the median of two input arrays of same length


def getMedianMerge(a1, a2):
    p1 = 0
    p2 = 0
    merged = []
    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] < a2[p2]:
            merged.append(a1[p1])
            p1 += 1
        else:
            merged.append(a2[p2])
            p2 += 1
    if p1 < len(a1):
        merged += a1[p1:]
    elif p2 < len(a2):
        merged += a2[p2:]
    n = len(merged)
    if n % 2 == 1:
        return merged[int(n/2)]
    else:
        return (merged[int(n/2)-1] + merged[int(n/2)])/2


def getMedian(a1, a2):
    return None


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6]
    print(getMedianMerge(arr1, arr2))
