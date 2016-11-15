class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need, found = collections.Counter(p), collections.Counter()
        ans, cnt, b = [], 0, 0
        for i, c in enumerate(s):
            found[c] += 1
            if c in need and found[c] <= need[c]:
                cnt += 1
            else:
                if c not in need:
                    cnt = 0
                    found.clear()
                    b = i+1
                else:
                    while found[c] > need[c]:
                        found[s[b]] -= 1
                        cnt -= found[s[b]] < need[c]
                        b += 1
            if cnt == len(p):
                ans.append(b)
        return ans
