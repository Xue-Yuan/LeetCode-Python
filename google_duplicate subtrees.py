from collections import defaultdict


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def deserialize(data):
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


def duplicate_subtree(root):
    m = defaultdict(list)

    def preorder(node):
        if not node:
            return '#'
        l, r = preorder(node.left), preorder(node.right)
        res = '{} {} {}'.format(node.val, l, r)
        m[res].append(node)
        return res

    preorder(root)
    for k, v in m.items():
        print k, v


if __name__ == '__main__':
    root = deserialize('10,6,5,4,#,#,3,#,#,4,#,#,7,5,4,#,#,3,#,#,#')
    duplicate_subtree(root)
