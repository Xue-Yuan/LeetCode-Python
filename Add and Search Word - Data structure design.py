class TrieNode(object):
    def __init__(self):
        self.m = {}
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if ch not in node.m:
                node.m[ch] = TrieNode()
            node = node.m[ch]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def _search(word, node):
            for idx, ch in enumerate(word):
                if ch != '.':
                    if ch not in node.m:
                        return False
                    node = node.m[ch]
                else:
                    for _, nxt in node.m.items():
                        if _search(word[idx+1:], nxt):
                            return True
                    return False
            return node.isWord

        return _search(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
