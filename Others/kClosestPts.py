"""
Given a list of points, return the k closest points to the origin.
"""

import math
import heapq


def getDist(A, B):
    return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)


def getKClosestPtsSimple(points, k):
    # O(nlogn) solution
    distances = []
    ptsMap = {}
    for pt in points:
        dist = getDist(pt, [0, 0])
        distances.append(dist)
        ptsMap[dist] = pt
    distances.sort()
    return [ptsMap[d] for d in distances[0:k]]


def getKClosestPtsEfficient(points, k):
    # O(k + (n-k)logk) solution
    # using a max heap (algo doesnt reflect bc of use of library functions)
    ptsMap = {}
    distances = []
    for pt in points:
        dist = getDist(pt, [0, 0])
        distances.append(dist)
        ptsMap[dist] = pt
    return [ptsMap[d] for d in heapq.nsmallest(k, distances)]


if __name__ == "__main__":
    pts = [(1, 1), (2, 3), (4, 2), (-1, 2)]
    print(getKClosestPtsSimple(pts, 2))
    print(getKClosestPtsEfficient(pts, 2))
