"""
Find the min number of arrows to burst all balloons
"""


def findMinArrowShots(points):
    # base cases
    if len(points) <= 1:
        return len(points)
    # sort the points by the ending x coordinate
    points.sort(key=lambda x: x[1])
    cur_end = points[0][1]
    arrows = 1
    for b in points:
        # if start of b is greater than cur_end --> we need new arrow
        # and the cur_end gets updated
        if b[0] > cur_end:
            arrows += 1
            cur_end = b[1]
    return arrows
