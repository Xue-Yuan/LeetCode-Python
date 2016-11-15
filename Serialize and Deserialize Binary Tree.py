# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(node):
            if not node:
                ans.append('#')
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            root = TreeNode(val)
            root.left = dfs()
            root.right = dfs()
            return root
        vals = iter(data.split(','))
        return dfs()


class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans, stk = [], []
        while stk or root:
            while root:
                stk.append(root)
                ans.append(str(root.val))
                root = root.left
            ans.append('#')
            root = stk.pop().right
        return ' '.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dummy, cur = TreeNode(0), None
        stk = [dummy]
        for val in data.split():
            if cur:
                if val != '#':
                    cur.left = TreeNode(int(val))
                stk.append(cur)
                cur = cur.left
            elif stk:
                cur = stk.pop()
                if val != '#':
                    cur.right = TreeNode(int(val))
                cur = cur.right
        return dummy.right
