class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        self.mins = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.vals.append(x)
        self.mins.append(min(self.mins[-1], x))

    def pop(self):
        """
        :rtype: void
        """
        self.vals.pop()
        self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.vals[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
