import collections
from typing import List


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = ans = 0
        min_q = collections.deque()
        max_q = collections.deque()
        for h, num in enumerate(nums):
            while min_q and nums[min_q[-1]] >= num:
                min_q.pop()
            min_q.append(h)
            while max_q and nums[max_q[-1]] <= num:
                max_q.pop()
            max_q.append(h)
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                l += 1
                if max_q[0] < l:
                    max_q.popleft()
                if min_q[0] < l:
                    min_q.popleft()
            ans = max(ans, h - l + 1)
        return ans
