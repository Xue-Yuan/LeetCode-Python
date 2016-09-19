class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0]*n for _ in range(n)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        b = self.board
        n, b[row][col] = len(b), player
        if (sum(chess == player for chess in b[row]) == n or
                sum(b[r][col] == player for r in range(n)) == n or
                row == col and sum(b[i][i] == player for i in range(n)) == n or
                row+col == n-1 and sum(b[i][n-i-1] == player for i in range(n)) == n):
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

