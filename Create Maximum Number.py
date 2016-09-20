class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        for i in range(k+1):
            if i <= len(nums1) and 0 <= k-i <= len(nums2):
                n1 = self._maxFromOne(nums1, i)
                n2 = self._maxFromOne(nums2, k-i)
                ans = max(ans, self._merge(n1, n2))
        return ans

    def _maxFromOne(self, nums, n):
        remain, stk = len(nums), []
        for num in nums:
            while remain > n and stk and stk[-1] < num:
                stk.pop()
                remain -= 1
            stk.append(num)
        return stk[:n]

    def _merge(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            ans.append(max(nums1, nums2).pop(0))
        return ans


if __name__ == '__main__':
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print Solution().maxNumber(nums1, nums2, k)
    nums1 = [2, 5, 6, 4, 4, 0]
    nums2 = [7, 3, 8, 0, 6, 5, 7, 6, 2]
    k = 15
    [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]
    print Solution()._merge(nums1, nums2)
    # print Solution().maxNumber(nums1, nums2, k)
