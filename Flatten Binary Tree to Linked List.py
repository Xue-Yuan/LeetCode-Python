# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def _flatten(root):
            if not root:
                return None
            l_end = _flatten(root.left)
            r_end = _flatten(root.right)
            if l_end:
                l_end.right = root.right
                root.right = root.left
                root.left = None
            return r_end or l_end or root

        _flatten(root)


class Solution2(object):
    """Preorder traversal
    """
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stk = [root] if root else []
        while stk:
            cur = stk.pop()
            if cur.right:
                stk += cur.right,
            if cur.left:
                stk += cur.left,
            cur.left, cur.right = None, stk[-1] if stk else None
