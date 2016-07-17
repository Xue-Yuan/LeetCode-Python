class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #the default will be evaluated only once and be shared with
        # subsequent calls
        def dfs(l, r, cur, ret=[]):
            if r == n:
                ret.append(cur)
            if l < n:
                dfs(l+1, r, cur+'(')
            if r < l:
                dfs(l, r+1, cur+')')
            return ret
        return dfs(0, 0, '')
