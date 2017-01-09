#coding: utf-8


"""String找最短substring 使得substring中的字符只包含 ‘a' 'b' 'c' 一次，其他字符不管。 没有就返回 “”
"""


def solution(s):
    beg = end = 0
    cnta = cntb = cntc = 0
    ans = ''
    for end in range(len(s)):
        cnta += s[end] == 'a'
        cntb += s[end] == 'b'
        cntc += s[end] == 'c'
        while cnta > 1 or cntb > 1 or cntc > 1 or s[beg] not in 'abc':
            cnta -= s[beg] == 'a'
            cntb -= s[beg] == 'b'
            cntc -= s[beg] == 'c'
            beg += 1
        if cnta == cntb == cntc == 1:
            ans = s[beg:end+1] if not ans else min(ans, s[beg:end+1], key=len)
    return ans


if __name__ == '__main__':
    print solution('aaabccc')
