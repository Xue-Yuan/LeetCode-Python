class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board, *self._next_available(board, 0, 0))

    def dfs(self, board, row, col):
        if row > 8:
            return True
        valid = [True] * 9
        self._get_valid(board, valid, row, col)
        for i in range(1, 10):
            if valid[i-1]:
                board[row][col] = str(i)
                nxt_r, nxt_c = self._next_available(board, row, col)
                if self.dfs(board, nxt_r, nxt_c):
                    return True
                board[row][col] = '.'
        return False

    def _get_valid(self, board, valid, row, col):
        for i in range(9):
            if board[row][i] != '.':
                valid[int(board[row][i])-1] = False
            if board[i][col] != '.':
                valid[int(board[i][col])-1] = False
            b_r, b_c = row//3*3 + i/3, col//3*3 + i%3
            if board[b_r][b_c] != '.':
                valid[int(board[b_r][b_c])-1] = False

    def _next_available(self, board, row, col):
        while row < 9 and board[row][col] != '.':
            row += col == 8
            col = (col+1) % 9
        return row, col


if __name__ == '__main__':
    b = [
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9'],
    ]
    solution = Solution()
    solution.solveSudoku(b)
    for row in b:
        print row
