# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        def lower_bound(b, e, target):
            while b < e:
                m = (b+e)/2
                if intervals[m][0].start >= target:
                    e = m
                else:
                    b = m+1
            return b
        intervals = [(interval, idx) for idx, interval in enumerate(intervals)]
        intervals.sort(key=lambda x: x[0].start)
        ans = [-1] * len(intervals)
        for i, (interval, idx) in enumerate(intervals):
            ret = lower_bound(i+1, len(intervals), interval.end)
            if ret < len(intervals):
                ans[idx] = intervals[ret][1]
        return ans
