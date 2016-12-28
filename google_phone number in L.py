#coding: utf-8
"""先介绍了chess里面knight是走L字形的。然后有一个电话拨号键盘：
1 2 3
4 5 6
7 8 9
  0
输入是这个键盘上的一个数字+想要拨的号的长度，从这个数字开始每一步都要走L字,
返回有多少种号码可以拨
"""


graph = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}


def solution(start, steps, memo={}):
    if (start, steps) not in memo:
        if steps == 0:
            memo[start, steps] = 1
        else:
            cnt = 0
            for nxt in graph[start]:
                cnt += solution(nxt, steps-1)
            memo[start, steps] = cnt
    return memo[start, steps]


if __name__ == '__main__':
    print solution(1, 1)
    print solution(1, 2)
    assert(solution(1, 5) == solution(3, 5))
    for i in range(1, 10):
        assert(solution(5, i) == 0)
    print solution(0, 3)
