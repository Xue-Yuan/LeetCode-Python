class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_sz, t_sz = len(s), len(t)
        if abs(s_sz - t_sz) > 1 or s == t:
            return False
        idx = 0
        while idx < min(s_sz, t_sz):
            if s[idx] != t[idx]:
                break
            idx += 1
        if s_sz == t_sz:
            return s[idx+1:] == t[idx+1:]
        if s_sz > t_sz:
            s, t = t, s
        return s[idx:] == t[idx+1:]
