"""
Given a list of people with their birth years and death years, find the year
with the highest population.
"""


def maxAlive(arr):
    aliveMap = {}
    for yearPair in arr:
        aliveMap[yearPair[0]] = 0
        aliveMap[yearPair[1]] = 0
    for yearPair in arr:
        aliveMap[yearPair[0]] += 1
        aliveMap[yearPair[1]] -= 1
    sorted_years = list(aliveMap.keys())
    sorted_years.sort()
    num_alive = 0
    max_alive = 0
    for y in sorted_years:
        num_alive += aliveMap[y]
        if num_alive > max_alive:
            max_alive = num_alive
    return max_alive


def main():
    arr = [(2000, 2010), (1975, 2005), (1975, 2003), (1803, 1809), (1750, 1869),
           (1840, 1935), (1803, 1921), (1894, 1921)]
    print(maxAlive(arr))


if __name__ == "__main__":
    main()
