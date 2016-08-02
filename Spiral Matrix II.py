class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top = left = 0
        bot = right = n-1
        ret = [[0 for _ in range(n)] for _ in range(n)]
        iota = self.iota(n)
        while top <= bot and left <= right:
            for c in range(left, right+1):
                ret[top][c] = iota.next()
            top += 1
            for r in range(top, bot+1):
                ret[r][right] = iota.next()
            right -= 1
            for c in range(right, left-1, -1):
                ret[bot][c] = iota.next()
            bot -= 1
            for r in range(bot, top-1, -1):
                ret[r][left] = iota.next()
            left += 1
        return ret

    def iota(self, n):
        for i in xrange(1, n*n+1):
            yield i
