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
        self.ans = float('-inf')

        def postOrder(node):
            if not node:
                return 0
            l, r = postOrder(node.left), postOrder(node.right)
            self.ans = max(
                self.ans, l+node.val, r+node.val, l+r+node.val, node.val
            )
            return max(l, r, 0) + node.val

        postOrder(root)
        return self.ans
