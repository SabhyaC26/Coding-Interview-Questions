"""
Input -> long string of the numbers in pi and list of fav numbers
Output -> min number of spaces that need to break up number to be in list
of fav numbers
"""


def splitPi(pi, favs):
    if pi == '':
        return 0
    else:
        for i in range(1, len(pi)+1):
            if pi[:i] in favs and splitPi(pi[i:], favs):
                return splitPi(pi[i:], favs) + 1
        return -1


def splitPiDP(pi, favs):
    pass
