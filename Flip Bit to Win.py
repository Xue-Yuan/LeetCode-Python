def solution(num):
    num = '{:b}'.format(num)
    sz = len(num)
    left, cnt = [], 0
    for n in num:
        if n == '1':
            cnt += 1
        else:
            left.append(cnt)
            cnt = 0
    ans = cnt = 0
    for n in reversed(num):
        if n == '1':
            cnt += 1
        else:
            ans = max(ans, left.pop()+cnt+1)
            cnt = 0
    return ans

print solution(1775)
