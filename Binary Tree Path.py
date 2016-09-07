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
