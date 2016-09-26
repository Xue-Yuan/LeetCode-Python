# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans, stk = 0, []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
                if root and not (root.left or root.right):
                    ans += root.val
            root = stk.pop().right
        return ans


def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    ans, stk = 0, []
    while stk or root:
        while root:
            stk.append(root)
            root = root.left
            if root and not (root.left or root.right):
                ans += root.val
        root = stk.pop().right
    return ans
