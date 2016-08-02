#DP timeout
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        opt = [0] + [-1] * (len(nums)-1)
        for i in range(1, len(nums)):
            for j in range(0, i+1):
                if i - j <= nums[j]:
                    if opt[i] < 0:
                        opt[i] = opt[j] + 1
                    else:
                        opt[i] = min(opt[i], opt[j]+1)
        return opt[-1]


class Solution2(object):
    def jump(self, nums):
        idx = cur = nxt = cnt = 0
        while idx <= cur:
            if cur >= len(nums) - 1:
                return cnt
            nxt = max(nxt, idx+nums[idx])
            if idx == cur:
                cur = nxt
                cnt += 1
            idx += 1
        return -1
