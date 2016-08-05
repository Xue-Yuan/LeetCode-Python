class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        c = len(matrix[0])
        heights = [0] * (c+1)
        ret = 0
        for row in matrix:
            for idx in range(c):
                heights[idx] = heights[idx]+1 if row[idx] == '1' else 0
            stk = []
            for idx, height in enumerate(heights):
                while stk and height < heights[stk[-1]]:
                    h = heights[stk.pop()]
                    w = idx if not stk else idx - stk[-1] - 1
                    ret = max(ret, w*h)
                stk.append(idx)
        return ret
