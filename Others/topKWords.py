"""
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower
alphabetical order comes first.
"""
import heapq


def topKFrequent(words, k):
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in wordCount.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
