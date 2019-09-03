"""
Return the k closest points to the origin
"""

import math


# simple sort approach
def kClosest(pts, K):
    pts.sort(key=lambda P: math.sqrt(P[0]**2 + P[1]**2))
    return pts[:K]


# now using divide and conquer
def kClosestDC(pts, K):
    pass
