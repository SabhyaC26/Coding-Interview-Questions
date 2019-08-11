def getTiles(area):
    lst = []
    while area != 0:
        val = int(math.sqrt(area))
        lst.append(val ** 2)
        area = area - (val ** 2)
    return lst
