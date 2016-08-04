class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        b = e = 0
        ret = ""
        need, found = Counter(t), Counter()
        cnt = 0
        while e < len(s):
            if s[e] in need:
                cnt += found[s[e]] < need[s[e]]
                found[s[e]] += 1
            e += 1
            while cnt == len(t):
                if not ret or e - b < len(ret):
                    ret = s[b:e]
                if s[b] in need:
                    cnt -= found[s[b]] <= need[s[b]]
                    found[s[b]] -= 1
                b += 1
        return ret
