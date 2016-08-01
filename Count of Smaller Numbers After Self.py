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
            ret[-1-idx] = cnt
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


# Taken from https://discuss.leetcode.com/topic/31162/mergesort-solution
class Solution2(object):
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
