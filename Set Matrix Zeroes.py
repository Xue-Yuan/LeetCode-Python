class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        row, col = len(matrix), len(matrix[0])

        def set_row_zero(r_no):
            for c in range(col):
                matrix[r_no][c] = 0

        def set_col_zero(c_no):
            for r in range(row):
                matrix[r][c_no] = 0

        first_row = first_col = False
        for c in range(col):
            first_row |= not matrix[0][c]
        for r in range(row):
            first_col |= not matrix[r][0]
        for r in range(row):
            for c in range(col):
                if not matrix[r][c]:
                    matrix[r][0] = matrix[0][c] = 0

        for c in range(1, col):
            if not matrix[0][c]:
                set_col_zero(c)
        for r in range(1, row):
            if not matrix[r][0]:
                set_row_zero(r)
        if first_row:
            set_row_zero(0)
        if first_col:
            set_col_zero(0)
