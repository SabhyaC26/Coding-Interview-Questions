def balancedSum(arr):
    total = 0
    for x in arr:
        total += x
    left_sum = 0
    for i in range(len(arr)):
        total -= arr[i]
        if left_sum == total:
            return i
        left_sum += arr[i]
    return -1


if __name__ == "__main__":
    a = [1, 2, 3, 4, 6]
    print(balancedSum(a))
