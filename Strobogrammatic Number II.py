m = [
    ('0', '0'),
    ('1', '1'),
    ('6', '9'),
    ('8', '8'),
    ('9', '6'),
]


class Solution(object):
    def findStrobogrammatic(self, n):
        ret, cur = [], [0]*n

        def dfs(b, e, cur):
            if b > e:
                ret.append(''.join(cur))
                return
            for i, j in m:
                cur[b], cur[e] = i, j
                if b == 0 and cur[b] == '0' and b != e:
                    continue
                if b == e and i != j:
                    continue
                dfs(b+1, e-1, cur)

        dfs(0, n-1, cur)
        return ret
