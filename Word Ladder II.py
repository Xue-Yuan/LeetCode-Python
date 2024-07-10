import collections
from typing import List
import string


class Solution:

    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        path = collections.defaultdict(list)
        lvl = {beginWord}
        wordSet = set(wordList)
        wordSet.discard(beginWord)

        while lvl:
            nxt = set()
            for w in lvl:
                if w == endWord:
                    break
                for i in range(len(w)):
                    for c in string.ascii_lowercase:
                        if c == w[i]:
                            continue
                        new_w = w[:i] + c + w[i + 1:]
                        if new_w in wordSet:
                            path[new_w].append(w)
                            nxt.add(new_w)
            lvl = nxt
            wordSet -= lvl

        sequences = []
        sequence = []

        def constructSequence(cur: str):
            sequence.append(cur)
            if cur == beginWord:
                sequences.append(list(reversed(sequence)))
                sequence.pop()
                return
            for parent in path[cur]:
                constructSequence(parent)
            sequence.pop()

        constructSequence(endWord)
        return sequences


class Solution2():
    """Bidirectional BFS
    """

    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        pathsaver = collections.defaultdict(list)
        w_len = len(beginWord)
        front, back = set([beginWord]), set([endWord])
        wordSet = set(wordList)
        wordSet.discard(endWord)
        wordSet.discard(beginWord)
        forward, done = True, False
        while front:
            nxt = set()
            for word in front:
                for idx in range(w_len):
                    for ch in string.ascii_lowercase:
                        if ch == word[idx]:
                            continue
                        newword = word[:idx] + ch + word[idx + 1:]
                        if newword in wordSet or newword in back:
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
            wordSet -= front
            wordSet -= back

        ret, path = [], [endWord]

        def constructladders(cur):
            """DFS building the path
            """
            if cur == beginWord:
                ret.append(list(reversed(path)))
            else:
                for word in pathsaver[cur]:
                    path.append(word)
                    constructladders(word)
                    path.pop()

        constructladders(endWord)
        return ret
