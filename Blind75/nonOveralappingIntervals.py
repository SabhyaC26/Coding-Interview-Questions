"""
Given a collection of intervals, find the minimum number of intervals you need
to remove to make the rest of the intervals non-overlapping.
"""


# unnecessary but makes code less ambigous
def getStart(pair):
    return pair[0]


# same as above
def getEnd(pair):
    return pair[1]


# removes all conflicting intervals for a given interval
def removeConflicts(activity, lst):
    lst.remove(activity)
    toRemove = []
    for pair in lst:
        if not(getEnd(pair) <= getStart(activity) or
               getStart(pair) >= getEnd(activity)):
            toRemove.append(pair)
    for pair in toRemove:
        lst.remove(pair)


def getMinIntervals(intervals):
    # this is essentially the clasic greedy question --> get the max
    # number of non-overlapping intervals: n-max is the answer we need

    # we are using the EFT algorithm
    # first sort the intervals by finish time
    ORIGINAL_INTERVAL_LENGTH = len(intervals)
    intervals = sorted(intervals, key=lambda x: x[1])
    maxSet = []
    while len(intervals) != 0:
        maxSet.append(intervals[0])
        removeConflicts(intervals[0], intervals)
    return ORIGINAL_INTERVAL_LENGTH - len(maxSet)


if __name__ == "__main__":
    ints = [[1, 100], [11, 22], [1, 11], [2, 12]]
    print(getMinIntervals(ints))
