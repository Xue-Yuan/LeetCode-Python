import re


def decompress(s):
    try:
        idx = s.index('[')
        l = r = 0
        for i in range(idx, len(s)):
            l += s[i] == '['
            r += s[i] == ']'
            if l == r:
                break
        return s[:idx-2] + int(s[idx-2]) * decompress(s[idx+1:i]) + decompress(s[i+1:])
    except:
        return s

print decompress('aaabbbccc2x[ab]ccc3x[abc2x[bcd]]aaa')
