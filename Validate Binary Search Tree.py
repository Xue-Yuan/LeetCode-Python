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


class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, max_val, min_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return dfs(node.left, node.val, min_val) and dfs(node.right, max_val, node.val)
        return dfs(root, float('inf'), float('-inf'))
