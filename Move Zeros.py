class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for num in nums:
            if num:
                nums[cur] = num
                cur += 1
        nums[cur:] = [0 for _ in range(cur, len(nums))]


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print nums
