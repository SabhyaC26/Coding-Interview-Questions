import math

# create a function that finds the k closest points from the vertex


def calcDist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def kClosesPts(pts, vtx, k):
    dists = {}
    for point in pts:
        dists[calcDist(point, vtx)] = point
    vals = list(dists.keys())
    vals.sort()
    return [dists[val] for val in vals[0:k]]


def main():
    points = [[1, 2], [2, 3], [1, -3]]
    vertex = [2, 2]
    k = 2
    print(kClosesPts(points, vertex, k))


if __name__ == "__main__":
    main()
