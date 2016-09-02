class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        for i in range(1 << n):
            ret.append(i ^ (i >> 1))
        return ret
