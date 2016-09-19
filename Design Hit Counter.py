class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lru = collections.deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        lru = self.lru
        if lru and timestamp == lru[0][0]:
            lru[0][1] += 1
        else:
            lru.appendleft([timestamp, 1])
            if len(lru) > 300:
                lru.pop()

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        return sum(
            cnt for time, cnt in self.lru
            if timestamp - time < 300
        )


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)