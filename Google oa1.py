#http://www.1point3acres.com/bbs/thread-168419-1-1.html


class Solution(object):

    def largestNumber(self, X):
        s = str(X)
        pos = 0
        for idx in range(1, len(s)):
            if s[idx-1] <= s[idx]:
                pos = idx
            else:
                break
        return int(s[:pos]+s[pos]+s[pos:])
