class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        t = len(nums1) + len(nums2)
        l, r = (t+1)//2, (t+2)//2
        return (self.kth(nums1, nums2, l) + self.kth(nums1, nums2, r)) / 2.
    
    def kth(self, n1, n2, k):
        if len(n1) > len(n2):
            n1, n2 = n2, n1
        if not n1:
            return n2[k-1]
        if k == 1:
            return min(n1[0], n2[0])
        i = min(len(n1), k//2)
        j = k - i
        if n1[i-1] > n2[j-1]:
            return self.kth(n1[:i], n2[j:], k-j)
        else:
            return self.kth(n1[i:], n2[:j+1], k-i)
