# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        def dfs(node, cntr, cur):
            if not node:
                return 0
            cur += node.val
            cnt = 0
            if cur - sum in cntr:
                cnt += cntr[cur-sum]
            cntr[cur] += 1
            cnt += dfs(node.left, collections.Counter(cntr), cur) + dfs(node.right, cntr, cur)
            return cnt
        return dfs(root, collections.Counter([0]), 0)


class Solution2(object):
    """To avoid copying the hash map.
    """
    def pathSum(self, root, sum):
        def dfs(node, cntr, cur):
            if not node:
                return 0
            cur += node.val
            cnt = 0
            if cur - sum in cntr:
                cnt += cntr[cur-sum]
            cntr[cur] += 1
            cnt += dfs(node.left, cntr, cur) + dfs(node.right, cntr, cur)
            cntr[cur] -= 1
            return cnt
        return dfs(root, collections.Counter([0]), 0)
