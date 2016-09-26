class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
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


class Solution2(object):
    """Bidirectional BFS
    """
    def ladderLength(self, beginWord, endWord, wordList):
        front, end = set([beginWord]), set([endWord])
        charset = list(string.lowercase)
        cnt = 2
        while front:
            tmp = set()
            for w in front:
                for idx, ch in enumerate(w):
                    for c in charset:
                        if ch == c:
                            continue
                        new = w[:idx] + c + w[idx+1:]
                        if new in end:
                            return cnt
                        if new in wordList:
                            tmp.add(new)
                            wordList.discard(new)
            front = tmp
            if len(front) > len(end):
                front, end = end, front
            cnt += 1
        return 0
