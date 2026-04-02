"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        res = 0
        
        intervals.sort(key=lambda i: i.start)
        prevEnd = intervals[0].end

        for inter in intervals[1:]:
            if inter.start < prevEnd:
                return False
            else:
                prevEnd = inter.end
        return True

