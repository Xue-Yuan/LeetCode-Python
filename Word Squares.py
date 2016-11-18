class TrieNode(object):
    def __init__(self):
        self.m = {}
        self.isWord = False


def insert(root, word):
    if not root:
        root = TrieNode()
    cur = root
    for ch in word:
        if ch not in cur.m:
            cur.m[ch] = TrieNode()
        cur = cur.m[ch]
    cur.isWord = True
    return root


def word_generator(prefix, root):
    for ch in prefix:
        if ch not in root.m:
            return
        root = root.m[ch]

    def dfs(node, path):
        if node.isWord:
            yield path
            return
        for ch in node.m:
            for res in dfs(node.m[ch], path+ch):
                yield res

    for res in dfs(root, ''):
        yield prefix + res


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words:
            return []
        sz = len(words[0])
        grid = [''] * sz

        root = None
        for word in words:
            root = insert(root, word)

        def get_prefix(row):
            prefix = ''
            for col in range(row):
                prefix += grid[col][row]
            return prefix

        def dfs(row, ans):
            if row >= sz:
                ans.append(grid[:])
                return ans
            for res in word_generator(get_prefix(row), root):
                grid[row] = res
                dfs(row+1, ans)
            return ans

        return dfs(0, [])
