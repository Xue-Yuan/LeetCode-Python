def is_magical(s, beg, end, m):
    if (beg, end) in m:
        return m[(beg, end)]
    cnt = 0
    for i in range(beg, end):
        cnt += 1 if s[i] == '1' else -1
        if cnt < 0:
            m[(beg, end)] = False
            return False
    m[(beg, end)] = cnt == 0
    return cnt == 0


def solution(s):
    m = {}
    ans, sz = s, len(s)
    for beg in range(0, sz):
        for mid in range(beg+1, sz):
            for end in range(mid+1, sz):
                if (s[beg:end] < s[mid:end]+s[beg:mid] and
                        is_magical(s, beg, mid, m) and
                        is_magical(s, mid, end, m)):
                    ans = max(ans, s[:beg]+s[mid:end]+s[beg:mid]+s[end:])
    return ans


if __name__ == '__main__':
    assert(solution('11011000') == '11100100')
    assert(solution('1100') == '1100')
    assert(solution('1101001100') == '1101001100')
