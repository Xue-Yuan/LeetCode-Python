class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2:
            return 0
        mi, ma = min(nums), max(nums)
        if mi == ma:
            return 0
        # The size of the buckets is greater than the size of nums.
        # So at least one bucket will be empty. The maximumGap will
        # lie between buckets
        buckets = [(-1, -1)] * (size + 1)
        for num in nums:
            idx = (num - mi) * (size + 1) // (ma - mi + 1)
            cur_mi, cur_ma = buckets[idx]
            cur_ma = max(cur_ma, num)
            cur_mi = num if cur_mi < 0 else min(num, cur_mi)
            buckets[idx] = (cur_mi, cur_ma)

        ans, prev = 0, None
        for bucket in [bucket for bucket in buckets if bucket[0] > 0]:
            if prev:
                ans = max(bucket[0] - prev[1], ans)
            prev = bucket
        return ans
