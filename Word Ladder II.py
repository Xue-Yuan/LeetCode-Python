class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[str]]
        """
        pathsaver = collections.defaultdict(list)
        w_len = len(beginWord)
        cur = set([beginWord])
        charset = string.lowercase
        wordlist.add(endWord)
        wordlist.discard(beginWord)
        while cur:
            nxt = set()
            for word in cur:
                for idx in range(w_len):
                    for ch in charset:
                        if ch == word[idx]:
                            continue
                        newword = word[:idx] + ch + word[idx+1:]
                        if newword in wordlist:
                            pathsaver[newword].append(word)
                            nxt.add(newword)
            if endWord in nxt:
                break
            cur = nxt
            wordlist -= cur

        ret, path = [], [endWord]

        def constructladders(cur):
            if cur == beginWord:
                ret.append(path[:])
            else:
                for word in pathsaver[cur]:
                    path.append(word)
                    constructladders(word)
                    path.pop()

        constructladders(endWord)
        for item in ret:
            item.reverse()
        return ret


class Solution2(object):
    """Bidirectional BFS
    """
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[str]]
        """
        pathsaver = collections.defaultdict(list)
        w_len = len(beginWord)
        front, back = set([beginWord]), set([endWord])
        charset = list(string.lowercase)
        wordlist.discard(endWord)
        wordlist.discard(beginWord)
        forward, done = True, False
        while front:
            nxt = set()
            for word in front:
                for idx in range(w_len):
                    for ch in charset:
                        if ch == word[idx]:
                            continue
                        newword = word[:idx] + ch + word[idx+1:]
                        if newword in wordlist or newword in back:
                            if forward:
                                pathsaver[newword].append(word)
                            else:
                                pathsaver[word].append(newword)
                            done |= newword in back
                            nxt.add(newword)
            if not nxt or done:
                break
            front = nxt
            if len(front) > len(back):
                front, back = back, front
                forward = not forward
            wordlist -= front
            wordlist -= back

        ret, path = [], [endWord]

        def constructladders(cur):
            """DFS building the path
            """
            if cur == beginWord:
                ret.append(path[:])
            else:
                for word in pathsaver[cur]:
                    path.append(word)
                    constructladders(word)
                    path.pop()

        constructladders(endWord)
        for item in ret:
            item.reverse()
        return ret
