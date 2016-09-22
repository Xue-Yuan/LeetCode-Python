class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        found = collections.Counter()
        b, cnt, ans = 0, 0, ''
        for idx, ch in enumerate(s):
            if ch in need:
                found[ch] += 1
                cnt += found[ch] <= need[ch]
                while cnt == len(t):
                    if not ans or len(ans) > idx-b+1:
                        ans = s[b:idx+1]
                    if s[b] in need:
                        cnt -= found[s[b]] <= need[s[b]]
                        found[s[b]] -= 1
                    b += 1
        return ans
