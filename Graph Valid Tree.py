class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        def _dfs(cur, pre):
            if cur in visited:
                return False
            visited.add(cur)
            for nxt in graph[cur]:
                if pre != nxt:
                    if not _dfs(nxt, cur):
                        return False
            return True
        return _dfs(0, -1) and len(visited) == n
