# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def _sortedArrayToBST(beg, end):
            if beg >= end:
                return None
            mid = (beg+end) >> 1
            root = TreeNode(nums[mid])
            root.left = _sortedArrayToBST(beg, mid)
            root.right = _sortedArrayToBST(mid+1, end)
            return root

        return _sortedArrayToBST(0, len(nums))
