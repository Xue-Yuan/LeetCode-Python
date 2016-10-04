class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def _dfs(cur, visited=set()):
            if cur in visited:
                return 0
            visited.add(cur)
            map(_dfs, graph[cur])
            return 1

        return sum(_dfs(cur) for cur in range(n))
