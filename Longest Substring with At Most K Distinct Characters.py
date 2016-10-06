class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cntr = collections.defaultdict(int)
        beg, ans = 0, 0
        for idx, ch in enumerate(s):
            cntr[ch] += 1
            while len(cntr) > k:
                cntr[s[beg]] -= 1
                if cntr[s[beg]] == 0:
                    del cntr[s[beg]]
                beg += 1
            ans = max(ans, idx-beg+1)
        return ans
