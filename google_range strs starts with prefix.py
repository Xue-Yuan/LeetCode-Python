"""Given a sorted list of string and a prefix, find the beginning and
end indices for the range that start with this prefix.
"""


def solution(strs, prefix):
    def search(b, e, check):
        while b < e:
            m = (b+e) >> 1
            if check(strs[m], prefix):
                b = m+1
            else:
                e = m
        return b

    start = search(
        0, len(strs),
        lambda a, b: len(a) < len(b) or a[:len(b)] < b)
    end = search(
        start, len(strs),
        lambda a, b: a.startswith(b))
    return [start, end]


strs = ['aaa', 'asdf', 'asdf', 'eqwrq', 'ieru', 'asdjf', 'uyeq']
strs.sort()
print strs
prefix = 'asd'
print solution(strs, prefix)
