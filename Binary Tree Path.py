# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        ans, path, stk = [], [], []
        pre = None
        while stk or root:
            if root:
                stk.append(root)
                path.append(str(root.val))
                root = root.left
            else:
                cur = stk.pop()
                if not cur.right or pre == cur.right:
                    if not cur.left and not cur.right:
                        ans.append('->'.join(path))
                    pre = cur
                    path.pop()
                else:
                    stk.append(cur)
                    root = cur.right
        return ans


class Solution2:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def _dfs(node, path, ret=[]):
            path.append(str(node.val))
            if not node.left and not node.right:
                ret.append('->'.join(path))
            else:
                if node.left:
                    _dfs(node.left, path)
                if node.right:
                    _dfs(node.right, path)
            path.pop()
            return ret
        return _dfs(root, []) if root else []
