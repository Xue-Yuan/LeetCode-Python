class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(beg, target, path, ans=[]):
            if target == 0:
                ans.append(path[:])
                return ans
            for idx in range(beg, len(candidates)):
                if idx == beg or candidates[idx] != candidates[idx-1]:
                    if target - candidates[idx] >= 0:
                        path.append(candidates[idx])
                        dfs(idx+1, target-candidates[idx], path)
                        path.pop()
            return ans
        candidates.sort()
        return dfs(0, target, [])
