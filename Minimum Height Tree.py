class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        indegrees = [0] * n
        adjacencies = [[] for _ in range(n)]
        for u, v in edges:
            indegrees[u] += 1
            indegrees[v] += 1
            adjacencies[v].append(u)
            adjacencies[u].append(v)
        q = collections.deque(i for i, v in enumerate(indegrees) if v == 1)
        while n > 2:
            sz = len(q)
            for _ in range(sz):
                v = q.popleft()
                n -= 1
                indegrees[v] -= 1
                for a in adjacencies[v]:
                    indegrees[a] -= 1
                    if indegrees[a] == 1:
                        q.append(a)
        return list(q)
