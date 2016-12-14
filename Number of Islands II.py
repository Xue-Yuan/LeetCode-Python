class UnionFind(object):
    def __init__(self):
        self.cnt = 0
        self.id = {}
        self.rank = {}

    def __contains__(self, pos):
        return pos in self.id

    def unite(self, p, q):
        p, q = self.find(p), self.find(q)
        if q == p:
            return
        s_p, s_q = self.rank[p], self.rank[q]
        if s_p > s_q:
            self.id[q] = p
        elif s_p < s_q:
            self.id[p] = q
        else:
            self.id[p] = q
            self.rank[q] += 1
        self.cnt -= 1

    def find(self, p):
        if self.id[p] == p:
            return p
        self.id[p] = self.find(self.id[p])
        return self.id[p]

    def add(self, p):
        self.id[p] = p
        self.rank[p] = 1
        self.cnt += 1


class Solution(object):
    def numIslands2(self, m, n, positions):
        ans = []
        islands = UnionFind()
        for p in map(tuple, positions):
            islands.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands:
                    islands.unite(p, q)
            ans += [islands.cnt]
        return ans
