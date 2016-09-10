class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        mid = len(nums) / 2
        nums[::2], nums[1::2] = nums[mid:], nums[:mid]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 1, 1, 6, 4]
    s.wiggleSort(nums)
    print nums
    nums = [1, 3, 2, 2, 3, 1]
    s.wiggleSort(nums)
    print nums
