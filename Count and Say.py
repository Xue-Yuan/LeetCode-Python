class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(1, n):
            beg = end = 0
            new = ''
            while beg < len(s):
                while end < len(s) and s[beg] == s[end]:
                    end += 1
                new += str(end-beg) + s[beg]
                beg = end
            s = new
        return s
