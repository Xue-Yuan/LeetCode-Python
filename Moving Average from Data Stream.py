class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        num, q = 0, self.q
        if len(q) == self.size and q:
            num = q.popleft()
        q.append(val)
        self.sum += val - num
        return 1.0*self.sum / len(q) if q else 0

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
