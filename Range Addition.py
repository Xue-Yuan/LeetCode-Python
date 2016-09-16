class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0] * (length+1)
        for b, e, v in updates:
            ans[b] += v
            ans[e+1] -= v
        cur = 0
        for idx in range(len(ans)):
            cur += ans[idx]
            ans[idx] = cur
        return ans[:-1]
