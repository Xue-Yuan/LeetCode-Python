class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        ans, h = [], [(nums1[0]+nums2[0], 0, 0)]
        while h and len(ans) < k:
            _, i1, i2 = heapq.heappop(h)
            ans.append((nums1[i1], nums2[i2]))
            if i1+1 < len(nums1):
                heapq.heappush(h, (nums1[i1+1]+nums2[i2], i1+1, i2))
            if i1 == 0 and i2+1 < len(nums2):
                heapq.heappush(h, (nums1[i1]+nums2[i2+1], i1, i2+1))
        return ans
