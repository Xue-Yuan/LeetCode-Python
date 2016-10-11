class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        ans = []
        for e in envelopes:
            idx = bisect.bisect_left(ans, e[1])
            if idx == len(ans):
                ans.append(e[1])
            else:
                ans[idx] = e[1]
        return len(ans)
