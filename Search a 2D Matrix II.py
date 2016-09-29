class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        x, y = 0, col-1
        while 0 <= x < row and 0 <= y < col:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        return False


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0]) if matrix else 0
        return self._search(matrix, 0, row-1, 0, col-1, target)
    
    def _search(self, matrix, r_beg, r_end, c_beg, c_end, target):
        if r_beg == r_end and c_beg == c_end:
            return matrix[r_beg][c_beg] == target
        if not (r_beg <= r_end and c_beg <= c_end):
            return False
        r_mid = (r_beg + r_end) >> 1
        c_mid = (c_beg + c_end) >> 1
        can = matrix[r_mid][c_mid]
        if can == target:
            return True
        elif can > target:
            return (
                self._search(matrix, r_beg, r_mid, c_beg, c_mid, target) or
                self._search(matrix, r_beg, r_mid, c_mid+1, c_end, target) or
                self._search(matrix, r_mid+1, r_end, c_beg, c_mid-1, target)
            )
        else:
            return (
                self._search(matrix, r_beg, r_mid, c_mid+1, c_end, target) or
                self._search(matrix, r_mid+1, r_end, c_beg, c_mid, target) or
                self._search(matrix, r_mid+1, r_end, c_mid+1, c_end, target)
            )
