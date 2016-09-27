class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans += n & 0x1
            n >>= 1
        return ans


class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            cnt += 1
            n = n & (n-1)
        return cnt
