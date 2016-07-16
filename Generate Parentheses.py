class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        def dfs(l, r, cur):
            if r == n:
                ret.append(cur)
            if l < n:
                dfs(l+1, r, cur+'(')
            if r < l:
                dfs(l, r+1, cur+')')
            return ret
        return dfs(0, 0, '')
