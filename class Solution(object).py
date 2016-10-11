class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(cur, n, ans):
            if cur <= n:
                ans.append(cur)
            for i in range(10):
                if cur*10+i > n:
                    return
                dfs(cur*10+i, n, ans)

        ans = []
        for i in range(1, 10):
            dfs(i, n, ans)
        return ans
