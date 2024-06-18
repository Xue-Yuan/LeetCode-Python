import collections


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def verticalOrder(self, root: TreeNode):
        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, i = queue.popleft()
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]


class Solution2:

    def verticalOrder(self, root: TreeNode):
        cols = collections.defaultdict(list)
        lvl = [(root, 0)]
        while lvl:
            tmp = []
            for node, col in lvl:
                cols[col].append(node)
                if node.left:
                    tmp.append((node.left, col - 1))
                if node.right:
                    tmp.append((node.right, col + 1))
            lvl = tmp
        return [cols[i] for i in sorted(cols)]
