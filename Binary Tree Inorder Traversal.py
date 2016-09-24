# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stk = [], []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            ret.append(root.val)
            root = root.right
        return ret


class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return list(self._inorder(root))

    def _inorder(self, root):
        stk = []
        while root or stk:
            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                yield root.val
                root = root.right
