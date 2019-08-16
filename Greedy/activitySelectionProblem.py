"""
Given a set S of activities with start time and finish time of each activity, find the maximum number of activities that can be performed by a single person assuming that a person can only work on a single activity at a time.
"""


def getStart(pair):
    return pair[0]


def getEnd(pair):
    return pair[1]


def removeConflicts(activity, lst):
    lst.remove(activity)
    toRemove = []
    for pair in lst:
        if not(getEnd(pair) <= getStart(activity) or
               getStart(pair) >= getEnd(activity)):
            toRemove.append(pair)
    for pair in toRemove:
        lst.remove(pair)


def getMaxActivities(activities):
    maxSet = []
    while len(activities) != 0:
        maxSet.append(activities[0])
        removeConflicts(activities[0], activities)
    return len(maxSet), maxSet


def main():
    set1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
            (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    max1, a1 = getMaxActivities(set1)
    print(max1, a1)


if __name__ == "__main__":
    main()
