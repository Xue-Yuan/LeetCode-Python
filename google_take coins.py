#coding: utf-8


"""一个array [1,5,3,8,10] 这样，代表n堆硬币，两个人每次可以取头上的或者尾巴上
的硬币，最后拿的总和最多的人获胜，求先手的最优策略。。。我只写了个递归的，面试时
间到了没来得及写dp的，都怪第一题。。。
"""


def min_max(arr):
    memo_max = {}
    memo_min = {}

    def max_val(arr, b, e):
        if b > e:
            return 0
        if b == e:
            return arr[b]
        if (b, e) not in memo_max:
            memo_max[b, e] = max(
                arr[b]+min_val(arr, b+1, e),
                arr[e]+min_val(arr, b, e-1),
                )
        return memo_max[b, e]

    def min_val(arr, b, e):
        if b > e:
            return 0
        if b == e:
            return arr[b]
        if (b, e) not in memo_min:
            memo_min[b, e] = min(
                max_val(arr, b+1, e),
                max_val(arr, b, e-1),
                )
        return memo_min[b, e]

    return max_val(arr, 0, len(arr)-1)


def dp(arr):
    l = len(arr)
    opt = [[0] * l for _ in range(l)]
    for b in range(l)[::-1]:
        for e in range(b, l):
            if b == e:
                opt[b][e] = arr[b]
            elif b+1 == e:
                opt[b][e] = max(arr[b], arr[e])
            else:
                opt[b][e] = max(
                    arr[b] + min(opt[b+1][e-1], opt[b+2][e]),
                    arr[e] + min(opt[b+1][e-1], opt[b][e-2]),
                    )
    return opt[0][-1]


if __name__ == '__main__':
    arr = [1,5,3,8,10]
    print min_max(arr)
    print dp(arr)
