class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def longest(s, ch, k):
            cnt, beg, ans = 0, 0, 0
            for i, c in enumerate(s):
                cnt += c != ch
                if cnt > k:
                    cnt -= s[beg] != ch
                    beg += 1
                ans = max(ans, i-beg+1)
            return ans
        return max(longest(s, ch, k) for ch in string.uppercase)
