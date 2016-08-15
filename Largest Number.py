class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums_str = [str(num) for num in nums]
        nums_str.sort(cmp=lambda x, y: cmp(x+y, y+x), reverse=True)
        return ''.join(nums_str).lstrip('0') or '0'
