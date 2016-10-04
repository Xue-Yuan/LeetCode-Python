# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _dfs(node):
            if not node:
                return 0, 0
            rob1, skip1 = _dfs(node.left)
            rob2, skip2 = _dfs(node.right)
            return node.val + skip1 + skip2, max(rob1, skip1) + max(rob2, skip2)
        return max(_dfs(root))
