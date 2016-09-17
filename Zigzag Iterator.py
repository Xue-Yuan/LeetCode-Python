class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = collections.deque([(v, 0) for v in (v1, v2) if v])

    def next(self):
        """
        :rtype: int
        """
        v, idx = self.q.popleft()
        if idx < len(v)-1:
            self.q.append((v, idx+1))
        return v[idx]

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
