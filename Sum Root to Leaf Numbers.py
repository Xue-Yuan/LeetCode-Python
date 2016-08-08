# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def preorder(root, s):
            s = s * 10 + root.val
            if not root.left and not root.right:
                return s
            val = 0
            if root.left:
                val += preorder(root.left, s)
            if root.right:
                val += preorder(root.right, s)
            return val

        return preorder(root, 0)


class Solution2(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stk, ans = [(root, root.val)], 0
        while stk:
            node, val = stk.pop()
            if node.right:
                stk.append((node.right, val*10+node.right.val))
            if node.left:
                stk.append((node.left, val*10+node.left.val))
            if not node.left and not node.right:
                ans += val
        return ans
