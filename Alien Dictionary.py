import collections


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        charset = set(''.join(words))
        indegrees = {x: 0 for x in charset}
        graph = {x: [] for x in charset}
        for pair in zip(words, words[1:]):
            for ch1, ch2 in zip(*pair):
                if ch1 != ch2:
                    graph[ch1].append(ch2)
                    indegrees[ch2] += 1
                    break
        q = collections.deque()
        for k, v in indegrees.items():
            if v == 0:
                q.append(k)
        ans = ''
        while q:
            cur = q.popleft()
            ans += cur
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    q.append(nxt)
            del graph[cur]
        return ans if not graph else ''


if __name__ == '__main__':
    solution = Solution()
    print solution.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
    print solution.alienOrder(['ak', 'bj'])
    print solution.alienOrder(["ab", "adc"])
