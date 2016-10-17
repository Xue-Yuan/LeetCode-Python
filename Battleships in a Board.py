class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not any(board):
            return 0
        row, col = len(board), len(board[0])
        visited = [[False] * col for _ in range(row)]
        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col) or visited[r][c] or board[r][c] != 'X':
                return 0
            visited[r][c] = True
            map(dfs, [r+1, r-1, r, r], [c, c, c+1, c-1])
            return 1
        return sum(dfs(r, c) for r in range(row) for c in range(col))
