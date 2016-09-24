class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i^(i>>1) for i in xrange(1<<n)]


class Solution2(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        t, ans = 1, [0]
        for _ in xrange(n):
            ans += [t|e for e in reversed(ans)]
            t <<= 1
        return ans
