# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stk = [], []
        while root or stk:
            while root:
                ret.append(root.val)
                stk.append(root)
                root = root.left
            root = stk.pop()
            root = root.right
        return ret
