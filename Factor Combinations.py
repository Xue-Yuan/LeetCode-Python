class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def _dfs(n, path, i, ret=[]):
            while i*i <= n:
                if n % i == 0:
                    path.append(i)
                    ret.append(path + [n/i])
                    _dfs(n/i, path, i)
                    path.pop()
                i += 1
            return ret
        return _dfs(n, [], 2)
