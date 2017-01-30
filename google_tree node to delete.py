#coding: utf-8

"""第一题，给一个tree，一个api，check一个node是不是要被delete，返回
被delete之后的tree的集合
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    def dfs():
        val = next(vals)
        if val == '#':
            return None
        root = TreeNode(int(val))
        root.left = dfs()
        root.right = dfs()
        return root
    vals = iter(data.split(','))
    return dfs()


delete_val = {2}


def to_delete(node):
    if not node:
        return False
    return node.val in delete_val


def solution(root):
    if not root:
        return None

    trees = {root}

    def dfs(node):
        if not node:
            return None
        if to_delete(node):
            trees.discard(node)
            if node.left:
                trees.add(node.left)
            if node.right:
                trees.add(node.right)
        node.left = dfs(node.left)
        node.right = dfs(node.right)
        return None if to_delete(node) else node

    dfs(root)
    return trees


def solution2(root):
    ans = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        if to_delete(node.left):
            node.left = None
        if to_delete(node.right):
            node.right = None
        if to_delete(node):
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
    dfs(root)
    if not to_delete(root):
        ans.append(root)
    return ans


def print_tree(root):
    if not root:
        return
    print root.val,
    print_tree(root.left)
    print_tree(root.right)


if __name__ == "__main__":
    root = deserialize("1,2,4,#,#,5,#,#,3,6,#,#,7,#,#")
    trees = solution2(root)
    for node in trees:
        print_tree(node)
        print
