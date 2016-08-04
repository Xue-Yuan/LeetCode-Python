class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(self.dfs(n, k, 1, []))

    def dfs(self, n, k, cur, path):
        if n - cur + 1 < k:
            return
        if k == 0:
            yield path[:]
            return
        path.append(cur)
        for p in self.dfs(n, k-1, cur+1, path):
            yield p
        path.pop()
        for p in self.dfs(n, k, cur+1, path):
            yield p


class Solution2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]
