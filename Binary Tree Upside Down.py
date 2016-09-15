# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        ret = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return ret


class Solution2(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        prev_left = prev_right = None
        while cur:
            nxt = cur.left
            cur.left = prev_right
            prev_right = cur.right
            cur.right = prev_left
            prev_left = cur
            cur = nxt
        return prev_left
