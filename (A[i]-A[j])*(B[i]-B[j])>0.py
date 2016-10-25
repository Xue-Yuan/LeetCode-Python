#coding: utf-8


"""给定两个长度一样的数字list A B,每个list都没有重复元素。判断他们是否满足如下性质:
对任意的 0<=i,j < len(A), (A[i]-A[j]) * (B[i]-B[j]) > 0
"""


def solution(A, B):
    A = sorted((num, idx) for idx, num in enumerate(A))
    B = sorted((num, idx) for idx, num in enumerate(B))
    return all(a[1] == b[1] for a, b in zip(A, B))
