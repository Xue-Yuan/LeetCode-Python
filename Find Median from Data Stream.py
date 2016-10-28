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
        s, l = self.heaps
        if len(s) == len(l):
            heapq.heappush(l, -heapq.heappushpop(s, -num))
        else:
            heapq.heappush(s, -heapq.heappushpop(l, num))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        s, l = self.heaps
        if len(s) == len(l):
            return (l[0] - s[0]) / 2.
        return l[0]

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
