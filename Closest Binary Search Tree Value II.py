"""
Given a non-empty binary search tree and a target value, find k values
in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST
that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n)
runtime (where n = total nodes)?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from heapq import heapify, heapreplace

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        pq, stk = [], []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            cur = stk.pop()
            if len(pq) < k:
                pq.append((-abs(target-cur.val), cur.val))
                if len(pq) == k:
                    heapify(pq)
            else:
                diff = abs(cur.val-target)
                if diff < -pq[0][0]:
                    heapreplace(pq, (-diff, cur.val))
            root = cur.right
        return [v for _, v in pq]


# O(k + log(n))
class Solution2(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        pre, suc = [], []
        while root:
            if root.val > target:
                suc.append(root)
                root = root.left
            else:
                pre.append(root)
                root = root.right
        ans = []
        for _ in range(k):
            if not pre:
                ans.append(self._getSuccessor(suc))
            elif not suc:
                ans.append(self._getPredecessor(pre))
            elif abs(pre[-1].val-target) < abs(suc[-1].val-target):
                ans.append(self._getPredecessor(pre))
            else:
                ans.append(self._getSuccessor(suc))
        return ans

    def _getPredecessor(self, pre):
        ret = cur = pre.pop()
        cur = cur.left
        while cur:
            pre.append(cur)
            cur = cur.right
        return ret.val

    def _getSuccessor(self, suc):
        ret = cur = suc.pop()
        cur = cur.right
        while cur:
            suc.append(cur)
            cur = cur.left
        return ret.val
