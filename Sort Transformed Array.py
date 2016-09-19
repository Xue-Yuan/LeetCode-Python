class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        nums = map(lambda x: a*x*x + b*x + c, nums)
        if a == 0:
            return nums if b >= 0 else nums[::-1]
        stk, beg, end = [], 0, len(nums)-1
        check = operator.gt if a > 0 else operator.lt
        while beg <= end:
            if check(nums[beg], nums[end]):
                stk.append(nums[beg])
                beg += 1
            else:
                stk.append(nums[end])
                end -= 1
        return stk if a < 0 else stk[::-1]
