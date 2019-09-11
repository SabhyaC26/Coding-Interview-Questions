def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()
    s = s.replace(" ", "")
    new_s = ''
    for c in s:
        if c.isalnum():
            new_s += c
    p1 = 0
    p2 = len(new_s)-1
    while p1 < p2:
        if new_s[p1] != new_s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True
