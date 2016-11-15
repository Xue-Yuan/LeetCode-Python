# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.end)
        beg = cnt = 0
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[beg].end:
                cnt += 1
            else:
                beg = i
        return cnt
