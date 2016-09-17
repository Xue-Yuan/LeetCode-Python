"""Refer to Closet Binary Search Tree Value II.py
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        ans = None
        while root:
            if root.val > p.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans

    def inorderPredecessor(self, root, p):
        ans = None
        while root:
            if root.val < p.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans


#recursively
class Solution2(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if root.val > p.val:
            return self.inorderSuccessor(root.left, p) or root
        else:
            return self.inorderSuccessor(root.right, p)
