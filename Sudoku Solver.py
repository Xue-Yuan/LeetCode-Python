class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def solve(r, c):
            r, c = self.advance(board, r, c)
            if r == 9:
                return True
            valid = self.getValid(board, r, c)
            for i in range(1, 10):
                if valid[i]:
                    board[r][c] = str(i)
                    if solve(r, c):
                        return True
                    board[r][c] = '.'
            return False
        solve(0, 0)

    def advance(self, board, r, c):
        while True:
            if r > 8 or board[r][c] == '.':
                break
            r += c == 8
            c = (c+1) % 9
        return r, c

    def getValid(self, board, r, c):
        valid = [True] * 10
        for i in range(9):
            if board[r][i] != '.':
                valid[int(board[r][i])] = False
            if board[i][c] != '.':
                valid[int(board[i][c])] = False
            sr, sc = r/3*3+i/3, c/3*3+i%3
            if board[sr][sc] != '.':
                valid[int(board[sr][sc])] = False
        return valid


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
