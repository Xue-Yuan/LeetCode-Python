class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(n, beg, path, ans):
            if path:
                ans.append(path + [n])
            for i in range(beg, int(n**.5)+1):
                if n % i == 0:
                    path.append(i)
                    dfs(n/i, i, path, ans)
                    path.pop()
            return ans
        return dfs(n, 2, [], [])
