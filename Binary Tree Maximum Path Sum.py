# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _maxPathSum(node):
            """return max, end_at_node_max
            """
            if not node:
                return root.val, 0
            max_l, end_l = _maxPathSum(node.left)
            max_r, end_r = _maxPathSum(node.right)
            ans = max(max_l, max_r, end_l+end_r+node.val)
            end = max(max(end_l, end_r, 0) + node.val, 0)
            return ans, end

        if not root:
            return 0
        return _maxPathSum(root)[0]
