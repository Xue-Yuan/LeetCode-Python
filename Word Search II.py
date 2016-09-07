class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        root = {}
        for word in words:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['\0'] = '\0'
        row, col = len(board), len(board[0])
        ans = []

        def _dfs(r, c, node, path):
            if 0 <= r < row and 0 <= c < col:
                cur = board[r][c]
                if not cur or cur not in node:
                    return
                save, board[r][c] = board[r][c], ''
                path += save
                child = node[cur]
                if '\0' in child:
                    ans.append(path)
                    #avoid duplicates
                    del child['\0']
                _dfs(r+1, c, child, path)
                _dfs(r-1, c, child, path)
                _dfs(r, c+1, child, path)
                _dfs(r, c-1, child, path)
                board[r][c] = save

        for r in range(row):
            for c in range(col):
                _dfs(r, c, root, '')
        return ans


if __name__ == '__main__':
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v'],
    ]
    words = ["oath", "pea", "eat", "rain"]
    print Solution().findWords(board, words)
