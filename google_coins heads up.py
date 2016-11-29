#coding: utf-8


"""給一個double array (length n) 代表每個硬幣投出正面的機率, input k 求
n硬幣中 k個是正面的機率
"""


def solution(arr, k):
    sz = len(arr)
    dp = [[0] * (k+1) for _ in range(sz+1)]
    for i in range(1, sz+1):
        for j in range(min(k+1, i+1)):
            if i-1 >= j:
                dp[i][j] = dp[i-1][j]*(1-arr[i]) + dp[i-1][j-1]*arr[i]
    return dp[sz][k]
