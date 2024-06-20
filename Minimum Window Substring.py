import collections


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        found = collections.Counter()
        b, cnt, ans = 0, 0, ''
        for idx, ch in enumerate(s):
            found[ch] += 1
            cnt += found[ch] <= need[ch]
            while cnt == len(t):
                if not ans or len(ans) > idx - b + 1:
                    ans = s[b:idx + 1]
                cnt -= found[s[b]] <= need[s[b]]
                found[s[b]] -= 1
                b += 1
        return ans


class Solution2:
    '''Two pointers; sliding window.
    '''

    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        found = collections.Counter()
        sz_t = len(t)
        sz_s = len(s)
        total = 0
        l = h = 0
        ans = ''
        while h < sz_s:
            while h < sz_s and total < sz_t:
                # Move high pointer to find a substring that contains all
                # characters in t
                ch = s[h]
                found[ch] += 1
                if found[ch] <= need[ch]:
                    total += 1
                h += 1
            while l < sz_s and total == sz_t:
                # Move low pointer to make the substring smaller.
                if ans == '' or len(ans) > h - l:
                    ans = s[l:h]
                ch = s[l]
                found[ch] -= 1
                if found[ch] < need[ch]:
                    total -= 1
                l += 1
        return ans
