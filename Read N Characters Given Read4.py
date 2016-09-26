# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        idx = 0
        tmp = [''] * 4
        while idx < n:
            ret = read4(tmp)
            for i in range(min(ret, n-idx)):
                buf[idx] = tmp[i]
                idx += 1
            if ret < 4:
                return idx
        return idx
