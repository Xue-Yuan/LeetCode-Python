class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not any(board):
            return not word
        row, col = len(board), len(board[0])

        def dfs(word, r, c):
            if not word:
                return True
            if not (0 <= r < row and 0 <= c < col) or word[0] != board[r][c]:
                return False
            tmp, board[r][c] = board[r][c], '\0'
            word = word[1:]
            if any((dfs(word, r+1, c), dfs(word, r-1, c), dfs(word, r, c+1), dfs(word, r, c-1))):
                return True
            board[r][c] = tmp
            return False

        for r in range(row):
            for c in range(col):
                if dfs(word, r, c):
                    return True
        return False
