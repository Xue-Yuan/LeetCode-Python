class Solution(object):
    """Clockwise
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


class Solution2(object):
    """Anti-clockwise
    """
    def rotate(self, matrix):
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        matrix.reverse()


class Solution3(object):
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        s, e = 0, len(m)-1
        while s < e:
            for c in range(s, e):
                m[c][e], m[e][s+e-c], m[s+e-c][s], m[s][c] = (
                    m[s][c], m[c][e], m[e][s+e-c], m[s+e-c][s])
            s += 1
            e -= 1
