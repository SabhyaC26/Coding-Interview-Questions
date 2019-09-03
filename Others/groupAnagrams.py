from collections import defaultdict
"""
group the anagrams together
"""


def groupAangrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        count = [0 for _ in range(26)]
        for c in s:
            count[ord(c) - ord('a')] += 1
        anagrams[tuple(count)].append(s)
    return anagrams.values()
