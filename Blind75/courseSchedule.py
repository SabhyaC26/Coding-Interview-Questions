"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have
to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?
LeetCode Rating: Medium
Link: https://leetcode.com/problems/course-schedule/
"""

from collections import defaultdict
from collections import deque


# this is basically a topological sort question
# top sort is a cycle detection algo
def canFinish(numCourses, prerequisites):
    # using the adjacency list rep of a graph (note the use if defualtdict)
    graph = defaultdict(list)
    # map to track the indegrees of the courses
    indegrees = [0 for i in range(numCourses)]
    # populate the above two data structures
    for pair in prerequisites:
        graph[pair[0]].append(pair[1])
        indegrees[pair[0]] += 1
    # init topSorted list
    topSorted = []
    # init queue of nodes with zero degrees
    zeroDegree = deque()
    for i in range(numCourses):
        if indegrees[i] == 0:
            zeroDegree.append(i)
    while zeroDegree:
        node = zeroDegree.popleft()
        topSorted.append(node)
        # now for each node M with an edge E from N to M do
        for m in graph.keys():
            if graph[m] is not None:
                if node in graph[m]:
                    lst = graph[m]
                    lst.remove(node)
                    graph[m] = lst
                    if graph[m] == []:
                        zeroDegree.append(m)
    # now if the graph has even a single edge --> it has a cycle
    for m in graph.keys():
        if graph[m] != []:
            return False
    return True


if __name__ == "__main__":
    num, pres = 3, [[1, 0], [2, 0]]
    print(canFinish(num, pres))
