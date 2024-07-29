from typing import List


class Node:

    def __init__(self):
        self.m = {}
        self.is_word = False


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not any(board):
            return []
        root = Node()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.m:
                    node.m[ch] = Node()
                node = node.m[ch]
            node.is_word = True
        row, col = len(board), len(board[0])
        ans = []

        def _dfs(r, c, node, path):
            if 0 <= r < row and 0 <= c < col:
                cur = board[r][c]
                if not cur or cur not in node.m:
                    return
                save, board[r][c] = board[r][c], ''
                path += save
                child = node.m[cur]
                if child.is_word:
                    ans.append(path)
                    #avoid duplicates
                    child.is_word = False
                _dfs(r + 1, c, child, path)
                _dfs(r - 1, c, child, path)
                _dfs(r, c + 1, child, path)
                _dfs(r, c - 1, child, path)
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
    s = Solution()
    print(s.findWords(board, words))
