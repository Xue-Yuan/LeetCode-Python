"""Test case updated since my last submitting. If the second word is a
prefix of the previous word, then there is no valid order.
"""

from typing import List
import collections
import itertools


class Solution:

    def alienOrder(self, words: List[str]):
        charset = set(''.join(words))
        indegrees = {x: 0 for x in charset}
        graph = {x: [] for x in charset}
        for w1, w2 in itertools.pairwise(words):
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    graph[ch1].append(ch2)
                    indegrees[ch2] += 1
                    break
            else:
                if len(w1) > len(w2):
                    return ''

        q = collections.deque(k for k in charset if indegrees[k] == 0)
        ans = ''
        while q:
            cur = q.popleft()
            ans += cur
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    q.append(nxt)
        if any(val != 0 for _, val in indegrees.items()):
            return ''
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
    print(s.alienOrder(['ak', 'bj']))
    print(s.alienOrder(["ab", "adc"]))
    print(s.alienOrder(["x", "z", "x"]))
