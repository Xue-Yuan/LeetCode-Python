class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        least, most, sz = min(nums), max(nums), len(nums)
        if least == most:
            return 0
        # The size of the buckets is one greater than the size of nums.
        # Make sure the greatest num goes into the last bucket and the
        # least number goes into the first bucket.
        # So at least one bucket in the middle will be empty.
        # The maximumGap will lie between buckets
        buckets = [[sys.maxint, -sys.maxint] for _ in range(sz+1)]
        for num in nums:
            idx = ((num - least) * sz) // (most - least)
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        ans, pre = 0, least
        for bucket in filter(lambda x: x[0] != sys.maxint, buckets):
            ans = max(ans, bucket[0]-pre)
            pre = bucket[1]
        return ans
