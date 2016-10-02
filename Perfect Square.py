class Solution(object):
    opt = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        _opt = self.opt
        while len(_opt) <= n:
            _opt.append(min(_opt[-i*i] for i in range(1, int(len(_opt)**.5 + 1)))+1)
        return _opt[n]
