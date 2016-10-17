class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.']*n for _ in range(n)]
        cols = [False] * n
        dig1, dig2 = [False]*(2*n-1), [False]*(2*n-1)

        def available(row, i):
            return not (cols[i] or dig1[row+i] or dig2[n-row+i-1])

        def dfs(row, n, board, ans=[]):
            if row == n:
                ans.append([''.join(r) for r in board])
                return ans
            for i in range(n):
                if available(row, i):
                    board[row][i] = 'Q'
                    dig1[row+i] = dig2[n-row+i-1] = cols[i] = True
                    dfs(row+1, n, board)
                    board[row][i] = '.'
                    dig1[row+i] = dig2[n-row+i-1] = cols[i] = False
            return ans
        return dfs(0, n, board)
