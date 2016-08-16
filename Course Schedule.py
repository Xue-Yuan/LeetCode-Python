class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegrees, graph = [0] * numCourses, [[] for _ in range(numCourses)]
        for pre in prerequisites:
            indegrees[pre[0]] += 1
            graph[pre[1]].append(pre[0])

        dq = collections.deque()
        for idx, idg in enumerate(indegrees):
            if not idg:
                dq.append(idx)
                numCourses -= 1

        while dq:
            cur = dq.popleft()
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if not indegrees[nxt]:
                    dq.append(nxt)
                    numCourses -= 1

        return not numCourses
