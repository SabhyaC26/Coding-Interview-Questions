import queue

# method used to find the min cost of connecting many pieces of ropes
def connectRopes(ropes):
    ropesPQ = queue.PriorityQueue(maxsize=0)
    for rope in ropes:
        ropesPQ.put(rope)
    cost = 0
    while(ropesPQ.qsize() > 2):
        a = ropesPQ.get()
        b = ropesPQ.get()
        cost += a + b
        ropesPQ.put(a+b)
    cost += ropesPQ.get() + ropesPQ.get()
    return cost

def main():
    print("test1: " + str(connectRopes([20, 4, 8, 2])))
    print("test2: " + str(connectRopes([1, 2, 5, 10, 35, 89])))
    print("test3: " + str(connectRopes([2, 2, 3, 3])))

if __name__ == "__main__":
    main()
