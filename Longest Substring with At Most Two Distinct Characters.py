class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        beg, ans, window = 0, 0, collections.Counter()
        for end, ch in enumerate(s):
            window[ch] += 1
            while len(window) > 2:
                window[s[beg]] -= 1
                if window[s[beg]] == 0:
                    del window[s[beg]]
                beg += 1
            ans = max(ans, end-beg+1)
        return ans
