"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        new_intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(0, len(intervals)):
            if i != len(intervals)-1:
                if new_intervals[i].end > new_intervals[i+1].start:
                    return False
        return True
        
