class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegrees, graph = [0] * numCourses, [[] for _ in range(numCourses)]
        for f, s in prerequisites:
            indegrees[f] += 1
            graph[s].append(f)

        dq = collections.deque()
        for idx, idg in enumerate(indegrees):
            if idg == 0:
                dq.append(idx)
                numCourses -= 1

        ans = []
        while dq:
            cur = dq.popleft()
            ans.append(cur)
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    dq.append(nxt)
                    numCourses -= 1

        return ans if numCourses == 0 else []
