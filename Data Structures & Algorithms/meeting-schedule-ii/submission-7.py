"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start)
    
        endTimes = []
        for i in intervals:
            if endTimes and i.start >= endTimes[0]:
                heapq.heappop(endTimes)
            heapq.heappush(endTimes, i.end)
        
        return len(endTimes)