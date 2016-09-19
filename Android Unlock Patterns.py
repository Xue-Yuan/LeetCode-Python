class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visit = set()
        jump = {
            (1, 3): 2,
            (1, 9): 5,
            (1, 7): 4,
            (2, 8): 5,
            (3, 7): 5,
            (3, 9): 6,
            (4, 6): 5,
            (7, 9): 8,
        }

        def _dfs(left, cur):
            if left == 1:
                return 1
            visit.add(cur)
            ret = 0
            for nxt in range(1, 10):
                pair = (min(cur, nxt), max(cur, nxt))
                if (nxt not in visit and
                        (pair not in jump or jump[pair] in visit)):
                    ret += _dfs(left-1, nxt)
            visit.discard(cur)
            return ret

        return sum(
            (_dfs(left, 1) + _dfs(left, 2))*4 + _dfs(left, 5)
            for left in range(m, n+1)
        )
