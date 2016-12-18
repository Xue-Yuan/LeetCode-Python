class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort()
        sz = len(envelopes)
        ans = [1]
        for i in range(1, sz):
            val = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    val = max(val, ans[j]+1)
            ans.append(val)
        return max(ans)


class Solution2(object):
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
