"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda item:item.start)
        rooms = []
        heapq.heapify(rooms)

        for i in intervals:
            if rooms and i.start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i.end)
        return len(rooms)