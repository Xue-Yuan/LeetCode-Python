class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minVal = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)
        if not self.minVal:
            self.minVal.append(x)
        else:
            self.minVal.append(min(x, self.minVal[-1]))

    def pop(self):
        """
        :rtype: void
        """
        self.stk.pop()
        self.minVal.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()