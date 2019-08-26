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


def isAlienSorted(words, order):
    order_index = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i+1]
        # Find the first difference word1[k] != word2[k].
        for k in range(min(len(w1), len(w2))):
                    # If they compare badly, it's not sorted.
            if w1[k] != w2[k]:
                if order_index[w1[k]] > order_index[w2[k]]:
                    return False
                break
        else:
            # If we didn't find a first difference, the
            # words are like ("mat", "matte").
            if len(w1) > len(w2):
                return False
    return True


if __name__ == "__main__":
    words = ["kuvp", "q"]
    order = "ngxlkthsjuoqcpavbfdermiywz"
    print(isAlienSorted(words, order))
