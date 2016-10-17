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
        def overlap(i, n):
            if i.start > n.start:
                i, n = n, i
            return i.end >= n.start

        def merge2(i, n):
            return Interval(min(i.start, n.start), max(i.end, n.end))

        ans = []
        for i in intervals:
            if overlap(i, newInterval):
                newInterval = merge2(i, newInterval)
            else:
                if i.start > newInterval.start:
                    i, newInterval = newInterval, i
                ans.append(i)
        ans.append(newInterval)
        return ans
