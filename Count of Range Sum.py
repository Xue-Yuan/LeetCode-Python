"""Python BST gives TLE.
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.cnt = 0
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                node = Node(val)
            if node.val > val:
                node.left = _insert(node.left, val)
            elif node.val < val:
                node.right = _insert(node.right, val)
            node.cnt += 1
            return node
        self.root = _insert(self.root, val)

    def greater_than(self, val):
        def _greater_than(node, val):
            if not node:
                return 0
            if node.val == val:
                return node.right.cnt if node.right else 0
            elif node.val < val:
                return _greater_than(node.right, val)
            else:
                tmp = node.cnt - (node.left.cnt if node.left else 0)
                return _greater_than(node.left, val) + tmp
        return _greater_than(self.root, val)


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        tree = Tree()
        ans = _sum = 0
        for num in nums+[0]:
            i = tree.greater_than(_sum - lower)
            j = tree.greater_than(_sum - upper - 1)
            tree.insert(_sum)
            ans += j-i
            _sum += num
        return ans


#https://discuss.leetcode.com/topic/33770/short-simple-o-n-log-n
class Solution2(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def divid_conquer(prefix, beg, end):
            cnt = 0
            if beg+1 < end:
                mid = (beg + end) >> 1
                cnt = divid_conquer(prefix, beg, mid) + divid_conquer(prefix, mid, end)
                i = j = mid
                for half in prefix[beg:mid]:
                    while i < end and prefix[i] - half < lower:
                        i += 1
                    while j < end and prefix[j] - half <= upper:
                        j += 1
                    cnt += j-i
                prefix[beg:end] = sorted(prefix[beg:end])
            return cnt

        return divid_conquer(prefix, 0, len(prefix))
