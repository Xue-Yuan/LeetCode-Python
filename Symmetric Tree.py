# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def sym(l, r):
            if not l and not r:
                return True
            if l and r:
                return l.val == r.val and sym(l.left, r.right) and sym(l.right, r.left)
            return False
        return sym(root.left, root.right)


class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stk = [(root.left, root.right)]
        while stk:
            left, right = stk.pop()
            if not (left and right and left.val == right.val or not left and not right):
                return False
            if left and right:
                stk.append((left.left, right.right))
                stk.append((left.right, right.left))
        return True
