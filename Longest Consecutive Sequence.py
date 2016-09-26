class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, d = 0, set(nums)
        for num in nums:
            if num in d:
                cnt = 1
                left, right = num-1, num+1
                while left in d:
                    cnt += 1
                    d.discard(left)
                    left -= 1
                while right in d:
                    cnt += 1
                    d.discard(right)
                    right += 1
                ans = max(ans, cnt)
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
