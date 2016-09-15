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
