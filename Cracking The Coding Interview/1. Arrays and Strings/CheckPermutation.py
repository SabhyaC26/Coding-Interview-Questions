"""
Given two strings, write a method to check if one is a permutation of the other.
"""

def isPerm(s1, s2):
    # if lengths are different --> cant be permutation
    if len(s1) != len(s2):
        return False
    for c in s1:
        # if they do not have the same set of chars --> cant be permutations
        if c not in s2:
            return False
        # if the number of times a particular char occurs in the string is different --> cant be permutations
        elif s1.count(c) != s2.count(c):
            return False
    return True

def main():
    print(isPerm("SABHYA", "ASBHAY"))
    print(isPerm("SAB", "SAMMY"))
    print(isPerm("SABHYA", "SABHYC"))

if __name__ == "__main__":
    main()

