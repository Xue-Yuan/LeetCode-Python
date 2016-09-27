class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for ch in word:
            if ch not in cur.m:
                cur.m[ch] = TrieNode()
            cur = cur.m[ch]
        cur.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            if ch not in cur.m:
                return False
            cur = cur.m[ch]
        return cur.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for ch in prefix:
            if ch not in cur.m:
                return False
            cur = cur.m[ch]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
