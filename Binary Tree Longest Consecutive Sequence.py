# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _dfs(node, pre, cnt):
            if not node:
                return cnt
            if pre and node.val == pre.val+1:
                nxt = cnt + 1
            else:
                nxt = 1
            return max(
                cnt,
                _dfs(node.left, node, nxt),
                _dfs(node.right, node, nxt),
            )
        return _dfs(root, None, 0)
