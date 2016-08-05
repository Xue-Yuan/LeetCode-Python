class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        row, col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                if self.dfs(board, word, 0, r, c):
                    return True
        return False

    def dfs(self, board, word, idx, r, c):
        if idx == len(word):
            return True
        if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0])
                or word[idx] != board[r][c]):
            return False

        tmp, board[r][c], idx = board[r][c], "\0", idx+1
        ret = (self.dfs(board, word, idx, r+1, c) or self.dfs(board, word, idx, r-1, c)
               or self.dfs(board, word, idx, r, c+1) or self.dfs(board, word, idx, r, c-1))
        board[r][c] = tmp
        return ret
