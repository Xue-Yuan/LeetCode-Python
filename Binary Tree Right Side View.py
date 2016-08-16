# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, lvl = [], [root] if root else []
        while lvl:
            ans.append(lvl[-1].val)
            lvl = [child for node in lvl for child in (node.left, node.right) if child]
        return ans
