from heapq import heappushpop, heappush, heappop

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        first, second = self.heaps
        heappush(first, -heappushpop(second, num))
        if len(first) > len(second):
            heappush(second, -heappop(first))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        first, second = self.heaps
        if len(first) < len(second):
            return second[0]
        else:
            return (second[0] - first[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
