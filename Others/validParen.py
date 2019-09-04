# '(', ')', '{', '}', '[' ']'
def validParen(s):
    stack = []
    match = {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in match.keys():
            stack.append(c)
        elif not stack or match[stack.pop()] != c:
            return False
    return len(stack) == 0
