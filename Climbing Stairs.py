class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = range(n+1)
        for cur in range(3, n+1):
            opt[cur] = opt[cur-1] + opt[cur-2]
        return opt[n]


class Solution2(object):
    def climbStairs(self, n):
        opt = range(3)
        for _ in range(3, n+1):
            opt = opt[1:] + [opt[-1] + opt[1]]
        return opt[-1] if n > 2 else opt[n]
