#coding: utf-8


"""一个array，找到每个点的左边第一个比他自己大的值替换他自己，如果没有的就是他自己
不变。比如：9,8,7,8,4,3,10,9一遍下来之后就是9,9,8,9,8,4,10,10"""


def solution(nums):
    stk, ans = [float('-inf')], []
    for num in nums:
        while stk and stk[-1] <= num:
            stk.pop()
        if not stk:
            ans.append(num)
        else:
            ans.append(stk[-1])
        stk.append(num)
    return ans


print solution([9,8,7,8,4,3,10,9])
