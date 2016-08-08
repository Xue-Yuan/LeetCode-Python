class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        import string
        cnt, w_len = 2, len(beginWord)
        cur = set([beginWord])
        charset = list(string.lowercase)
        while cur:
            nxt = set()
            for word in cur:
                for idx in range(w_len):
                    for ch in charset:
                        newword = word[:idx] + ch + word[idx+1:]
                        if newword == endWord:
                            return cnt
                        if newword in wordList:
                            nxt.add(newword)
                            wordList.remove(newword)
            cnt += 1
            cur = nxt
        return 0
