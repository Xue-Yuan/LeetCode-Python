#coding: utf-8

"""第一题，给一个tree，一个api，check一个node是不是要被delete，返回
被delete之后的tree的集合
"""


def to_delete(node):
    pass


def solution(root):
    def dfs(node):
        if not node:
            return
        if to_delete(node):
            if node.left:
                descendant.append(node.left)
            if node.right:
                descendant.append(node.right)
        dfs(node.left)
        dfs(node.right)

    descendant = collections.deque([root] if root else [])
    ans = []
    while descendant:
        cur = descendant.popleft()
        ans.append(cur)
        dfs(cur)
    return ans
