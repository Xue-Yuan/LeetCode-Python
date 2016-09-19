# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        def _dfs(node):
            if not node:
                return -1
            lvl = max(_dfs(node.left), _dfs(node.right)) + 1
            if len(ans) == lvl:
                ans.append([])
            ans[lvl].append(node.val)
            return lvl
        _dfs(root)
        return ans
