def isMonotonic(A: List[int]) -> bool:
    if len(A) <= 2:
        return True
    inc = dec = True
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            inc = False
        if A[i] < A[i+1]:
            dec = False
    return inc or dec
