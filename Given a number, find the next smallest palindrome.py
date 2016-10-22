"""http://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/
"""


def solution(num):
    if all(i == '9' for i in num):
        return str(int(num)+2)
    sz = len(num)
    left, right = num[:sz/2+(sz&0x1)], num[sz/2:]

    def get(left):
        if sz & 0x1:
            return left[:-1] + left[-1] + left[:-1][::-1]
        return left + left[::-1]

    for l, r in zip(left[::-1], right):
        if l != r:
            left = str(int(left)+1) if l < r else left
            return get(left)
    left = str(int(left)+1)
    return get(left)


print solution('1221')
print solution('9')
print solution('999')
print solution('783322')
print solution('14587678322')
print solution('1234628')
print solution('12921')
print solution('125322')
print solution('94187978322')
