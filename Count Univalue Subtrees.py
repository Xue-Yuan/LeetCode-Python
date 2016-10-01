# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _dfs(node):
            if not node:
                return True
            left, right = _dfs(node.left), _dfs(node.right)
            if (left and right and
                    (not node.left or node.left.val == node.val) and
                    (not node.right or node.right.val == node.val)):
                self.cnt += 1
                return True
            return False
        self.cnt = 0
        _dfs(root)
        return self.cnt
