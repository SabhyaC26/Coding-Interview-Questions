"""
Given a string, write a function to check if it is a permutation of a palin­drome. A palindrome is a word or phrase that
is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited
to just dictionary words.

I really like this problem because of the simple, elegant solution that it uses
"""

# this is the main (and only) function needed to solve the problem


def palPerm(s):
    # basically --> we want to check if there exists a permutation of (s) that is a palindrome
    chars = []
    for c in s:
        if c not in chars:
            chars.append(c)
        else:
            chars.remove(c)
    if len(s) % 2 == 0:
        return len(chars) == 0
    else:
        return len(chars) == 1

# helper method to check if a given string is a palindrome
# turns out this function is not necessary for solving the problem
# i'll still leave it in there


def isPal(s):
    stack = []
    half = int(len(s)/2)
    # if even -> put 1/2 elts in the list
    if len(s) % 2 == 0:
        for x in range(half):
            stack.append(s[x])
        for x in range(half):
            if stack.pop() != s[x + half]:
                return False
    # if odd -> put all elts before the center elt
    else:
        for x in range(half):
            stack.append(s[x])
        for x in range(half):
            if stack.pop() != s[x + half + 1]:
                return False
    return True


def main():
    print(palPerm("hello"))  # should be false
    print(palPerm("RACECAR"))  # should be true
    print(palPerm("CARERACE"))  # should be true

    # print(isPal("ABA"))
    # print(isPal("MALAYALAM"))


if __name__ == "__main__":
    main()
