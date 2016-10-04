"""If we are allowed to add characters in both ends, then reverse it
and run the algorithm again
"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        re = s[::-1]
        for idx in range(len(s)+1):
            if s.startswith(re[idx:]):
                return re[:idx] + s


#KMP
class Solution2(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        new = s + '#' + r
        lps = [0] * len(new)
        for idx in range(1, len(new)):
            lnth = lps[idx-1]
            while lnth > 0 and new[lnth] != new[idx]:
                lnth = lps[lnth-1]
            lps[idx] = lnth + (new[lnth] == new[idx])
        return r[:len(r)-lps[-1]] + s
