class TreeNode(object):

    def __init__(self, val, cnt=1):
        self.val = val
        self.cnt = cnt
        self.left = None
        self.right = None


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        root = None
        ret = [0] * len(nums)
        for idx, num in enumerate(reversed(nums)):
            root, cnt = self.insert(root, num)
            ret[~idx] = cnt
        return ret

    def insert(self, root, val):
        if not root:
            return TreeNode(val), 0
        if val == root.val:
            ret = root.left.cnt if root.left else 0
        elif val > root.val:
            tmp = root.cnt - (root.right.cnt if root.right else 0)
            root.right, ret = self.insert(root.right, val)
            ret += tmp
        else:
            root.left, ret = self.insert(root.left, val)
        root.cnt += 1
        return root, ret


class Solution2(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = [0] * len(nums)
        self._mergeSort(list(enumerate(nums)), smaller)
        return smaller

    def _mergeSort(self, nums, smaller):
        mid = len(nums) / 2
        if mid:
            left = self._mergeSort(nums[:mid], smaller)
            right = self._mergeSort(nums[mid:], smaller)
            i = j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                    nums[i+j] = left[i]
                    smaller[left[i][0]] += j
                    i += 1
                else:
                    nums[i+j] = right[j]
                    j += 1
        return nums

