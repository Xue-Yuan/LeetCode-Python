"""Clockwise
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


"""Anti-clockwise
"""


class Solution2(object):
    def rotate(self, matrix):
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        matrix.reverse()
