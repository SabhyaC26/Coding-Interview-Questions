"""
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower
alphabetical order comes first.
"""
import heapq


def topKFrequent(words, k):
    wordCount = {}
    for w in words:
        if w not in wordCount.keys():
            wordCount[w] = 0
        wordCount[w] += 1
    h = []
    for key, value in wordCount.items():
        if len(h) < k:
            heapq.heappush(h, (value, key))
        else:
            top = heap[0]
            if top[0] < value:
                heapq.heappop(h)
                heapq.heappush(h, (value, key))
    return [x[1] for x in h]
