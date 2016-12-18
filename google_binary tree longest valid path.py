#coding: utf-8


"""给一个二叉树，求出最长的valid path的长度，valid path的定义是：1.path中的元素都
是相邻的递增或者递减的，如［1，2，3，4。。］或者［4，3，2，1。。］，2.path的构成可以
是从child－parent－child也可以是不打折的path。
Follow－up：基于上题修改两个条件：1.这是一个一般的树，而不是二叉树；同时2.valid的序
列不一定是相邻的，任意间隔的等差数列都可以。
"""


class Solution(object):
    def firstQuestion(self, root):
        """For each node, return two int to indicate the length of
        the increasing sequence and the length of the decreasing
        sequence.
        """
        self.ans = 0

        def dfs(root):
            if not root:
                return 0, 0
            l_inc, l_dec = dfs(root.left)
            r_inc, r_dec = dfs(root.right)
            inc = dec = 1
            if l_inc and root.val == root.left.val + 1:
                inc = max(inc, l_inc+1)
            if l_dec and root.val == root.left.val - 1:
                dec = max(dec, l_dec+1)
            if r_inc and root.val == root.right.val + 1:
                inc = max(inc, r_inc+1)
            if r_dec and root.val == root.right.val - 1:
                dec = max(dec, r_dec+1)
            if root.left and root.right:
                if root.val == root.left.val + 1 == root.right.val - 1:
                    self.ans = max(self.ans, l_inc + 1 + r_dec)
                if root.val == root.left.val - 1 == root.right.val + 1:
                    self.ans = max(self.ans, l_dec + 1 + r_inc)
            self.ans = max(inc, dec, self.ans)
            return inc, dec

    def follow_up(self, root):
        """For each node, return a dictionary of `diff: length` mapping
        """
        self.ans = 0

        def dfs(root):
            if not root:
                return {}
            cur = collections.defaultdict(int)
            vec_d = [dfs(kid) for kid in root.kids]
            for kid, d in zip(root.kids, vec_d):
                if kid:
                    diff = root.val - kid.val
                    if diff in d:
                        cur[diff] = max(d[diff]+1, cur[diff])
                    else:
                        cur[diff] = max(cur[diff], 2)
            self.ans = max([self.ans] + [v for _, v in cur.items()])
            for k1, d1 in zip(root.kids, vec_d):
                for k2, d2 in zip(root.kids[1:], vec_d[1:]):
                    if k1 and k2 and root.val - k1.val == k2.val - root.val:
                        diff = root.val - k1.val
                        if diff in d1 and -diff in d2:
                            self.ans = max(self.ans, d1[diff] + d2[-diff] + 1)
                        if -diff in d1 and diff in d2:
                            self.ans = max(self.ans, d1[-diff] + d2[diff] + 1)
            return cur

        dfs(root)
        return self.ans
