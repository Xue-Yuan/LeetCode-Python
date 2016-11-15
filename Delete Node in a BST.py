# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def _delete(node, key):
            if not node:
                return None
            if node.val > key:
                node.left = _delete(node.left, key)
                return node
            elif node.val < key:
                node.right = _delete(node.right, key)
                return node
            else:
                if not node.right:
                    return node.left
                right = node.right
                while right.left:
                    right = right.left
                node.val = right.val
                node.right = _delete(node.right, right.val)
                return node
        return _delete(root, key)
