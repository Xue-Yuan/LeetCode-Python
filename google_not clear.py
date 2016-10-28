#coding: utf-8


"""第一轮:白人小哥,2D matrix从左上出发,只能走右上/右/右下三个方向,问到右上的路径数.
follow up如果要求某些点必须经过?给一个数组A,要求经过点的y坐标是A的子序列.都很快地
bug free写完并且滚动数组优化.follow up的时候指出可以用hash表替代set,聊了一会儿
红黑树和AVL=。=小哥好像很满意

Follow up: 存储路径，dfs重构路径并计数
"""


def solution1(row, col):
    grid = [[0] * col for _ in range(row)]
    grid[0][0] = 1
    for j in range(1, col):
        for i in range(row):
            grid[i][j] = grid[i][j-1]
            if i > 0:
                grid[i][j] += grid[i-1][j-1]
            if i < row-1:
                grid[i][j] += grid[i+1][j-1]
    return grid[0][-1]


print solution1(2, 2)
print solution1(1, 1)
print solution1(3, 3)


"""第三轮:三姐,首先是split一个句子,但是被""包围的子句要保留.讨论了很多
corner case,好像比较满意然后也bug free了.follow up,给一个同义词关系,
然后关系是单向的.然后判断俩句子意思是不是一样的.如果有词有多个意思怎么办?
"""


def solution3(s):
    """Assume legitimate
    """
    beg = end = 0
    ans = []
    s += ' '
    while end < len(s):
        if s[end] == '"':
            end += 1
            while s[end] != '"':
                end += 1
            ans.append(s[beg:end+1])
            beg = end = end+1
        else:
            if s[end] == ' ':
                if s[beg:end].strip():
                    ans.append(s[beg:end])
                beg = end = end+1
            else:
                end += 1
    return ans

print solution('"hi hi hi" hi hi')
