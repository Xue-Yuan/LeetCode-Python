class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.Counter(p)
        found = collections.Counter()
        total = 0
        b = 0
        ans = []
        for e, ch in enumerate(s):
            found[ch] += 1
            if found[ch] <= need[ch]:
                total += 1
            while found[ch] > need[ch]:
                found[s[b]] -= 1
                if found[s[b]] < need[s[b]]:
                    total -= 1
                b += 1
            if total == len(p):
                ans.append(b)
        return ans
