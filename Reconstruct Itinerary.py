class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for beg, end in sorted(tickets, reverse=True):
            graph[beg].append(end)

        def _dfs(beg, ans=[]):
            while graph[beg]:
                _dfs(graph[beg].pop())
            ans.append(beg)
            return ans

        return _dfs('JFK')[::-1]
