def solution(num):
    odds = num & 0x55555555
    evens = num & 0xAAAAAAAA
    return ((odds << 1) | (evens >> 1)) & 0xFFFFFFFF

print '{:032b}'.format(134122)
print '{:032b}'.format(solution(134122))
