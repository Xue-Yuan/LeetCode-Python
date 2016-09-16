"""
Given an array of meeting time intervals consisting of start and
end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum
number of conference rooms required.

For example,
    Given [[0, 30],[5, 10],[15, 20]],
    return 2.
"""
import heapq


class Interval(object):
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end


class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x.start)
        pq = [-1]
        for interval in intervals:
            if interval.start >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, interval.end)
        return len(pq) if intervals else 0


if __name__ == "__main__":
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    s = Solution()
    print s.minMeetingRooms(intervals)
