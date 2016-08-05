class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        opt = [1] + [0] * (len(s))
        for idx in range(1, len(s)+1):
            if s[idx-1] != "0":
                opt[idx] = opt[idx-1]
            if idx != 1 and "09" < s[idx-2:idx] < "27":
                opt[idx] += opt[idx-2]
        return opt[-1]
