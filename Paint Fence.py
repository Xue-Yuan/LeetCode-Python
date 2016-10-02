class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        opt = [0, k, k*k]
        for _ in range(n-1):
            opt.append((opt[-1]+opt[-2])*(k-1))
        return opt[n]


class Solution2(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        pre, cur = k, k*k
        if n < 3:
            return (0, pre, cur)[n]
        for _ in range(3, n+1):
            cur, pre = (cur+pre)*(k-1), cur
        return cur
