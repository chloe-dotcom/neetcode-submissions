"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        rooms = []
        for i in intervals:
            if rooms and i.start < rooms[-1].end:
                return False
            if not rooms or i.end > rooms[-1].end:
                rooms.append(i)
        
        return True