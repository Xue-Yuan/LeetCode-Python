# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = None
        for val in self._inorder(root):
            if prev is not None and prev >= val:
                return False
            prev = val
        return True

    def _inorder(self, node):
        if node:
            for val in self._inorder(node.left):
                yield val
            yield node.val
            for val in self._inorder(node.right):
                yield val
