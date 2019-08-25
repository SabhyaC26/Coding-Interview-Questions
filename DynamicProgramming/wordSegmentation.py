"""
Given an input string and a dictionary of words, find out if the input string
can be segmented into a space-separated sequence of dictionary words.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung"
or "i like sam sung".
"""

# first do recursive solution


def wordSegRec(s, words):
    if s == '':
        return True
    else:
        return any([(s[:i] in words) and wordSegRec(s[i:], words) for i in range(1, len(s)+1)])


# now we do a DP approach

def wordSegDP(s, words):
    # TODO


if __name__ == "__main__":
    d = {'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
         'cream', 'icecream', 'man', 'go', 'mango', 'and'}
    print(wordSegRec("ilikesamsung", d))
    print(wordSegRec("iiiiiiii", d))
    print(wordSegRec("", d))
    print(wordSegRec("ilikelikeimangoiii", d))
    print(wordSegRec("samsungandmango", d))
    print(wordSegRec("samsungandmangok", d))
