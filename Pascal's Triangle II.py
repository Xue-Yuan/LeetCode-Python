class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1] * (rowIndex+1)
        for row in range(2, (rowIndex+1)):
            for idx in range(1, row):
                ret[row-idx] += ret[row-idx-1]
        return ret
