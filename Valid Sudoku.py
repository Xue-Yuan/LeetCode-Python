class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row, col, block = [0]*9, [0]*9, [0]*9
        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if item != '.':
                    num = 1 << int(item)
                    if row[r] & num or col[c] & num or block[r//3*3+c//3] & num:
                        return False
                    row[r] |= num
                    col[c] |= num
                    block[r//3*3+c//3] |= num
        return True
