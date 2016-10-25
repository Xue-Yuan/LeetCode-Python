def solution(num, lvl, n):
    cur = (num, lvl+1-num)
    if lvl >= n:
        return '({}, {})'.format(*cur)
    return '({}, {})'.format(solution(num, lvl*2, n), solution(lvl+1-num, lvl*2, n))


print solution(1, 2, 8)
