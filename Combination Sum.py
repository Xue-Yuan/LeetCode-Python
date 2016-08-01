class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(candidates, 0, target, [], ret)
        return ret

    def dfs(self, can, idx, tar, cur, ret):
        for i in range(idx, len(can)):
            cur.append(can[i])
            tar -= can[i]
            if tar == 0:
                ret.append(cur[:])
            elif tar > 0:
                self.dfs(can, i, tar, cur, ret)
            cur.pop()
            tar += can[i]
