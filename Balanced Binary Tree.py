# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(root):
            if not root:
                return 0
            h_l, h_r = height(root.left), height(root.right)
            if h_l < 0 or h_r < 0 or abs(h_l - h_r) > 1:
                return -1
            return max(h_l, h_r)+1

        return height(root) >= 0
