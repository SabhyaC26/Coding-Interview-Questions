"""
In an alien language, surprisingly they also use english lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted lexicographicaly
in this alien language.

LeetCode Rating: Easy

Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
"""


# solution is slightly wrong - working on a fix
def isAlienSorted(words, order):
    # first create a reverse lookup table
    revLookup = {}
    for i in range(len(order)):
        revLookup[order[i]] = i
    # let's now give each word in words a lexographical rank
    lex_ranks = []
    smallest = words[0]
    for word in words:
        if len(word) < len(smallest):
            smallest = word
    for word in words:
        lex = 0
        for i in range(len(smallest)):
            lex += (revLookup[word[i]]+1)/(i+1)
        lex_ranks.append(lex)
    for i in range(len(lex_ranks)-1):
        if not (lex_ranks[i] <= lex_ranks[i+1]):
            return False
    return True


if __name__ == "__main__":
    words = ["kuvp", "q"]
    order = "ngxlkthsjuoqcpavbfdermiywz"
    print(isAlienSorted(words, order))
