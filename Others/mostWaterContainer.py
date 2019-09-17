def maxArea(height):
    l = 0
    r = len(height) - 1
    ans = float('-inf')
    while r > l:
        ans = max(ans, (r-l) * min(height[l], height[r]))
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
    return ans
