"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        intervals.sort(key= lambda i: i.start)
        heapq.heapify(rooms) # keep sorted in lowest to highest end

        for i in intervals:
            if rooms and i.start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i.end)
        
        return len(rooms)