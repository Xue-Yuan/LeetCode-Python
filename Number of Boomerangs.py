class Solution(object):
    def numberOfBoomerangs(self, points):
        ans = 0
        for p in points:
            m = defaultdict(int)
            for q in points:
                m[(p[0]-q[0])**2 + (p[1]-q[1])**2] += 1
            ans += sum(v*(v-1) for _, v in m.items())
        return ans
