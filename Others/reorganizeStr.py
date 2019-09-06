from collections import defaultdict


def reorganizeString(S: str) -> str:
    countMap = defaultdict(int)
    for c in S:
        countMap[c] += 1
