""" For O(n) solution, prove the following fact:
1. The longest sequence can always be achieved by including the first element;
2. Consecutive duplicates can be reduced to only one element without affecting
 the final answer;
3. The longest sequence can be achieved by including the imediate rising or
 falling.
"""

from typing import List


class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dpDown = [1] * n
        dpUp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dpUp[i] = max(dpUp[i], dpDown[j] + 1)
                elif nums[i] < nums[j]:
                    dpDown[i] = max(dpDown[i], dpUp[j] + 1)

        return max(dpUp[n - 1], dpDown[n - 1])
