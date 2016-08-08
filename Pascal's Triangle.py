class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [[1] * row for row in range(1, numRows+1)]
        for row in range(2, numRows):
            for idx in range(1, row):
                ret[row][idx] = ret[row-1][idx-1] + ret[row-1][idx]
        return ret
