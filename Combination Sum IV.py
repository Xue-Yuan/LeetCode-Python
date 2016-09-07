class Solution(object):
def combinationSum4(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    m = collections.Counter([0])

    def dfs(nums, beg, target):
        if target in m:
            return m[target]
        cnt = 0
        for idx, num in enumerate(nums):
            if num <= target:
                cnt += dfs(nums, idx, target-num)
        m[target] += cnt
        return cnt

    return dfs(nums, 0, target, 0)
