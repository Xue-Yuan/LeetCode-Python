'''https://www.geeksforgeeks.org/count-of-subarrays-having-exactly-k-distinct-elements/
'''

from typing import List
import collections


class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(k: int):
            ans = 0
            l = 0
            cntr = collections.Counter()
            num_distinct = 0
            for h, num in enumerate(nums):
                cntr[num] += 1
                if cntr[num] == 1:
                    num_distinct += 1
                while num_distinct > k:
                    cntr[nums[l]] -= 1
                    if cntr[nums[l]] == 0:
                        num_distinct -= 1
                    l += 1
                ans += h - l + 1
            return ans

        return atMostK(k) - atMostK(k - 1)


class Solution2:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cntr = collections.Counter()
        begin, prefix, cnt = 0, 0, 0
        res = 0

        for num in nums:
            # Increase the frequency
            cntr[num] += 1
            if cntr[num] == 1:
                cnt += 1
            if cnt > k:
                cntr[nums[begin]] -= 1
                begin += 1
                cnt -= 1
                prefix = 0
            while cntr[nums[begin]] > 1:
                cntr[nums[begin]] -= 1
                begin += 1
                prefix += 1
            if cnt == k:
                res += prefix + 1

        # Return the final count
        return res
