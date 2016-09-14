import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(dict)
        for (a, b), c in zip(equations, values):
            graph[a][b], graph[b][a] = c, 1/c
            graph[a][a] = graph[b][b] = 1

        def _dfs(beg, end, visited):
            if beg in graph:
                visited.add(beg)
                if end in graph[beg]:
                    return graph[beg][end]
                for mid in graph[beg]:
                    if mid not in visited:
                        res = graph[beg][mid] * _dfs(mid, end, visited)
                        if res > 0:
                            graph[beg][end] = res
                            return res
                visited.discard(beg)
            return -1.0

        return [_dfs(beg, end, set()) for beg, end in queries]


if __name__ == '__main__':
    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    print Solution().calcEquation(equations, values, queries)
