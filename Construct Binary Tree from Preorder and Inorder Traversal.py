# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.pidx = 0

        def _buildTree(beg, end):
            if beg >= end:
                return None
            root = TreeNode(preorder[self.pidx])
            self.pidx += 1
            root_idx = inorder.index(root.val)
            root.left = _buildTree(beg, root_idx)
            root.right = _buildTree(root_idx+1, end)
            return root

        return _buildTree(0, len(inorder))
