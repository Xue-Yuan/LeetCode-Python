class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def _dfs(can, idx, _sum, path, ans=[]):
            for cur in range(idx, len(can)):
                path.append(can[cur])
                if _sum + can[cur] == target:
                    ans.append(path[:])
                elif _sum + can[cur] < target:
                    _dfs(can, cur, _sum, path)
                path.pop()
            return ans
        candidates.sort()
        return _dfs(candidates, 0, 0, [])
