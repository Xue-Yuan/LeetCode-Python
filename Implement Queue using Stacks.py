class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk_in = []
        self.stk_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stk_in.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        _in, _out = self.stk_in, self.stk_out
        if not _out:
            while _in:
                _out.append(_in.pop())
        return _out.pop()

    def peek(self):
        """
        :rtype: int
        """
        _in, _out = self.stk_in, self.stk_out
        if not _out:
            while _in:
                _out.append(_in.pop())
        return _out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.stk_in or self.stk_out)
