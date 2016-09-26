# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.save = ['']*4
        self.end = 0
        self.start = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            if self.start == 0:
                self.end = read4(self.save)
            if self.end == 0:
                break
            while idx < n and self.start < self.end:
                buf[idx] = self.save[self.start]
                idx += 1
                self.start += 1
            if self.start == self.end:
                self.start = 0
        return idx
