# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans = []
        for interval in intervals:
            if self._overlap(interval, newInterval):
                newInterval = self._merge(interval, newInterval)
            else:
                if interval.start > newInterval.start:
                    newInterval, interval = interval, newInterval
                ans.append(interval)
        ans.append(newInterval)
        return ans

    def _overlap(self, interval1, interval2):
        if interval1.start > interval2.start:
            interval1, interval2 = interval2, interval1
        return interval1.end >= interval2.start

    def _merge(self, interval1, interval2):
        return Interval(min(interval1.start, interval2.start),
                        max(interval1.end, interval2.end))
