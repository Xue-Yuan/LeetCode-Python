class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(self.dfs(nums, 0, []))

    def dfs(self, nums, idx, path):
        if idx == len(nums):
            yield path[:]
            return
        for p in self.dfs(nums, idx+1, path):
            yield p
        path.append(nums[idx])
        for p in self.dfs(nums, idx+1, path):
            yield p
        path.pop()


class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(self.dfs(nums, 0, []))

    def dfs(self, nums, idx, path):
        yield path[:]
        for cur in range(idx, len(nums)):
            path.append(nums[cur])
            for p in self.dfs(nums, cur+1, path):
                yield p
            path.pop()


class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res


class Solution4(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        ret = self.subsets(nums[:len(nums)-1])
        ret += [item + [nums[-1]] for item in ret]
        return ret
