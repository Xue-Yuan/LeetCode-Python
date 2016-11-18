class Solution(object):
    def find132pattern(self, nums):
        stk, mid = [], float('-inf')
        for num in nums[::-1]:
            if num < mid:
                return True
            else:
                while stk and num > stk[-1]:
                    mid = max(mid, stk.pop())
            stk.append(num)
        return False


#How about 213 pattern?
def find213pattern(nums):
    stk, mid = [], float('inf')
    for num in nums:
        if num > mid:
            return True
        else:
            while stk and num < stk[-1]:
                mid = min(mid, stk.pop())
        stk.append(num)
    return False


#And 123?