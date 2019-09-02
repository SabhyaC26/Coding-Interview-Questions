"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

LeetCode Rating: Medium

Link: https://leetcode.com/problems/meeting-rooms-ii/
"""

import heapq


def minMeetingRooms(intervals):
    if len(intervals) <= 1:
        return len(intervals)
    # The heap initialization
    rooms = []
    # Sort the meetings in increasing order of their start time.
    intervals.sort(key=lambda x: x[0])
    # Add the first meeting
    heapq.heappush(rooms, intervals[0][1])
    # For all the remaining meeting rooms
    for i in intervals[1:]:
        # If room is free --> assign to this interval
        if rooms[0] <= i[0]:
            heapq.heappop(rooms)
        # If a new room is to be assigned --> add to heap
        # If an old room is allocated --> update and add to heap
        heapq.heappush(rooms, i[1])
    # Return heap size
    return len(rooms)
