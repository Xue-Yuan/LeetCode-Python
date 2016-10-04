# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        inf = float('inf')

        def _dfs(node):
            if not node:
                return 0, inf, -inf
            ans1, min1, max1 = _dfs(node.left)
            ans2, min2, max2 = _dfs(node.right)
            if max1 < node.val < min2:
                return ans1+ans2+1, min(min1, node.val), max(max2, node.val)
            return max(ans1, ans2), -inf, inf

        return _dfs(root)[0]
