# '(', ')', '{', '}', '[' ']'
def validParen(s):
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')' or c == '}' or c == ']':
            a = stack.pop()
            if c == ')':
                if a != '(':
                    return False
            elif c == '}':
                if a != '{':
                    return False
            elif c == ']':
                if a != '[':
                    return False
    return True
