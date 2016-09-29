class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        q = self.q
        q.append(x)
        sz = len(q)
        for _ in range(sz-1):
            q.append(q.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q
