class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _maxCoins(l, r):
            if (l, r) not in memo:
                if l+1 >= r:
                    return 0
                memo[l, r] = max(
                    nums[i]*nums[l]*nums[r]+_maxCoins(l, i)+_maxCoins(i, r)
                    for i in range(l+1, r)
                )
            return memo[l, r]
        nums = [1] + nums + [1]
        memo = {}
        return _maxCoins(0, len(nums)-1)


class Solution2(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        sz = len(nums)
        opt = [[0] * sz for _ in range(sz)]
        for l in range(2, sz):
            for i in range(sz):
                j = i+l
                if j <= sz-1:
                    opt[i][j] = max(
                        nums[i]*nums[j]*nums[k]+opt[i][k]+opt[k][j]
                        for k in range(i+1, j)
                    )
        return opt[0][sz-1]
