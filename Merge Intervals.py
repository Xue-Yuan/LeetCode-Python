# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        ret = []
        for interval in intervals:
            if ret and not self.isDisjoint(ret[-1], interval):
                ret[-1].end = max(interval.end, ret[-1].end)
            else:
                ret.append(interval)
        return ret

    def isDisjoint(self, a, b):
        return a.end < b.start or a.start > b.end
