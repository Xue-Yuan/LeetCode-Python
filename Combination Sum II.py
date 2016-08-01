class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return list(self.dfs(candidates, 0, target, []))

    def dfs(self, can, idx, tar, cur):
        for i in range(idx, len(can)):
            if i == idx or can[i] != can[i-1]:
                tar -= can[i]
                if tar == 0:
                    yield cur + [can[i]]
                elif tar > 0:
                    cur.append(can[i])
                    for rs in self.dfs(can, i+1, tar, cur):
                        yield rs
                    cur.pop()
                else:
                    break
                tar += can[i]
