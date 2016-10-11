class Solution(object):

    opt = [0, 10, 9*9]
    for i in range(3, 10+1):
        opt.append(opt[-1]*(11-i))

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(self.opt[:n+1]) if n else 1
