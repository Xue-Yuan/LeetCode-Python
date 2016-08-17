class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(b, k, n):
            if not k and not n:
                ans.append(pth[:])
            for num in range(b, 10):
                if n-num < 0:
                    break
                pth.append(num)
                dfs(num+1, k-1, n-num)
                pth.pop()

        ans, pth = [], []
        dfs(1, k, n)
        return ans
