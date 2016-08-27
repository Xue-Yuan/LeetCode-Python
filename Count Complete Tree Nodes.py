# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left, right = root.left, root.right
        lvl_l = lvl_r = 0
        while left:
            left = left.left
            lvl_l += 1
        while right:
            right = right.right
            lvl_r += 1
        if lvl_l == lvl_r:
            return (1 << (lvl_l+1)) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
