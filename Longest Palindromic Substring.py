class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def _left_and_right(left, right):
            while 0 <= left and right < sz and s[left] == s[right]:
                left, right = left-1, right+1
            return left, right

        beg, end, sz = 0, 0, len(s)
        for idx in range(sz):
            l, r = _left_and_right(idx-1, idx+1)
            if r-l-1 > end-beg:
                beg, end = l+1, r
            l, r = _left_and_right(idx, idx+1)
            if r-l-1 > end-beg:
                beg, end = l+1, r
        return s[beg:end]


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = '#'.join('^{}$'.format(s))
        P = [0] * len(T)
        R, C = 0, 0
        for i in range(1, len(T)-1):
            mirror_i = 2*C - i
            P[i] = min(R-i, P[mirror_i]) if R > i else 0
            while T[i+P[i]+1] == T[i-P[i]-1]:
                P[i] += 1
            if i + P[i] > R:
                R, C = i+P[i], i
        maxl, mid = max((l, idx) for idx, l in enumerate(P))
        return s[(mid-maxl)//2:(mid+maxl)//2]
