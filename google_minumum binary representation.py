#coding: utf-8


"""input: int n
function: 将n用2的指数表示，使得指数表达式的个数最少
output : int num（指数的最少个数）
e.g: input = 28
28 = 2^4 + 2^3 + 2^2  => num = 3
28 = 2^5 - 2^2             => num = 2.
所以 output = 2
"""


def solution(n):
    """个数就是len(add) + len(sub)
    """
    cnt = 0
    add, sub = [], []

    def countTrailingOnes(n):
        bit, ones = 0x1, 0
        while n & bit:
            bit <<= 1
            ones += 1
        return ones

    while n:
        if n & 0x1:
            ones = countTrailingOnes(n)
            if ones >= 2:
                sub.append(cnt)
                n += 1
            else:
                add.append(cnt)
                n >>= 1
        else:
            n >>= 1
            cnt += 1

    return (
        '+'.join(map(lambda x: '2^{}'.format(x), add)) + '-' +
        '-'.join(map(lambda x: '2^{}'.format(x), sub))
    )


if __name__ == '__main__':
    print solution(0b1101110)
    print solution(28)
