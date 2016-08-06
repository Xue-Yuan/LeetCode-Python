# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret, lvl = [], [root] if root else []
        while lvl:
            ret += [node.val for node in lvl],
            lvl = [child for node in lvl for child in (node.left, node.right) if child]
        ret.reverse()
        return ret
