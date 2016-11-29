def encode(s):
    def check_repeating(s):
        sz = len(s)
        lps = [0] * sz
        for i in range(1, sz):
            l = lps[i-1]
            while l and s[l] != s[i]:
                l = lps[l-1]
            lps[i] = l + (s[l] == s[i])
        if lps[-1] and sz % (sz-lps[-1]) == 0:
            p = sz - lps[-1]
            return sz/p, s[:p]
        return 1, s

    memo = {}

    def _encode(s):
        if s not in memo:
            if len(s) <= 2:
                return s
            can = s
            for m in range(1, len(s)-1):
                l_cnt, l_str = check_repeating(s[:m])
                r_cnt, r_str = check_repeating(s[m:])
                if l_str == r_str:
                    comb = '{}[{}]'.format(l_cnt+r_cnt, _encode(l_str))
                else:
                    comb = _encode(s[:m])+_encode(s[m:])
                can = min(can, comb, key=len)
            memo[s] = can
        return memo[s]

    return _encode(s)
