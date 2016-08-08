class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        m = collections.defaultdict(int)
        ans = 0
        for num in nums:
            if m[num] == 0:
                left, right = m[num-1], m[num+1]
                val = 1 + left + right
                m[num] = m[num-left] = m[num+right] = val
                ans = max(ans, val)
        return ans

# https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak/2
class Solution2:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                best = max(best, m - n)
        return best
