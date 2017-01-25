class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subset(beg, path, ans=[]):
            if len(path) >= 2:
                ans.append(path[:])
            visited = set()
            for idx in range(beg, len(nums)):
                if nums[idx] in visited:
                    continue
                if not path or nums[idx] >= path[-1]:
                    path.append(nums[idx])
                    visited.add(nums[idx])
                    subset(idx+1, path)
                    path.pop()
            return ans
        return subset(0, [])
