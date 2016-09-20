class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans, path = [], []
        def _dfs(start, end, remain):
            if not remain:
                ans.append(path[:])
            for cur in range(start, end):
                path.append(cur)
                _dfs(cur+1, end, remain-1)
                path.pop()
        _dfs(1, n+1, k)
        return ans
