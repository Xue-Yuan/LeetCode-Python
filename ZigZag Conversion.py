class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        l = [''] * numRows
        idx, direc = 0, 1
        for c in s:
            l[idx] += c
            if idx == numRows-1:
                direc = -1
            elif idx == 0:
                direc = 1
            idx += direc
        return ''.join(l)
