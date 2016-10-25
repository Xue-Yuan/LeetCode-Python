"""mean of array with min&max value removed
"""


def solution(nums):
    largest, smallest, sum = float('-inf'), float('inf'), 0
    l_cnt = s_cnt = 0
    for num in nums:
        if num > largest:
            largest = num
            l_cnt = 0
        if num < smallest:
            smallest = num
            s_cnt = 0
        l_cnt += largest == num
        s_cnt += smallest == num
        sum += num
    print largest, l_cnt, smallest, s_cnt
    return (sum-largest*l_cnt-smallest*s_cnt)/(len(nums)-l_cnt-s_cnt)


print solution([1,1,1,1,2,3,4,4,4])
