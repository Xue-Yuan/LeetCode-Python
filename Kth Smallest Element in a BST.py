# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(node):
            if node:
                for val in inorder(node.left):
                    yield val
                yield node.val
                for val in inorder(node.right):
                    yield val
        return next(itertools.islice(inorder(root), k-1, k))


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.cnt = 1
#         self.left = None
#         self.right = None

class SolutionModifiedTree(object):
    def kthSmallest(self, root, k):
        if root:
            left = root.left.cnt if root.left else 0
            right = root.right.cnt if root.right else 0
            if k < left:
                return self.kthSmallest(root.left, k)
            elif k == root.cnt - right:
                return root.val
            else:
                return self.kthSmallest(root.right, k-root.cnt+right)
