#coding: utf-8
'''Follow up是给一个list输入, A[i] < A[j], j-i is maximized，输出(i,j)'''

'''先从左到右遍历一边数组，得到当前位置最小的数及其index，然后再从右往左遍历一边，
得到当前最大的数及其索引。
然后从头开始比较两个组数'''
