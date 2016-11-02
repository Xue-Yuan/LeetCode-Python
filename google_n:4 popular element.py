#coding: utf-8


"""n/4 Popular Element，找Quartile，用binary search
"""


import bisect


def solution(nums):
    if not nums:
        return -1

    quarter = len(nums)/4

    def check(idx):
        num = nums[idx]
        start = bisect.bisect_left(nums, num, idx+1-quarter, idx+1)
        end = bisect.bisect_right(nums, num, idx, idx+quarter)
        return end-start >= quarter

    for idx in (quarter-1, quarter*2-1, quarter*3-1):
        if check(idx):
            return nums[idx]
    return -1


print solution([1,1,1,4,5,6,7,8,9,10,11])
