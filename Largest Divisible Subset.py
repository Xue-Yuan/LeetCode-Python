class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        vecs = []
        for num in sorted(nums):
            tmp = []
            for vec in vecs:
                if num % vec[-1] == 0 and len(vec) > len(tmp):
                    tmp = vec
            vecs.append(tmp + [num])
        return max(vecs, key=len) if vecs else []


class Solution2(object):
    """Or save the index only instead of the whole array
    """
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        sz, opt = len(nums), [1 for _ in nums]
        idx, indices = 0, [-1] * sz
        nums.sort()
        for i in range(sz):
            for j in range(i):
                if nums[i] % nums[j] == 0 and opt[j]+1 > opt[i]:
                    opt[i] = opt[j]+1
                    indices[i] = j
            if opt[i] > opt[idx]:
                idx = i
        ans = []
        while idx >= 0:
            ans.append(nums[idx])
            idx = indices[idx]
        return ans
