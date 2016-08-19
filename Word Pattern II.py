# Problem Description:

# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

# Examples:

# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.


class Solution(object):
    def wordPatternMatch(self, p, s):

        def dfs(p, s, m1, m2):
            if not p and s or not s and p:
                return False
            if not p and not s:
                return True
            for end in range(1, len(s)+1):  # for pruning, len(s)-end >= len(p)-1
                if p[0] not in m1 and s[:end] not in m2:
                    m1[p[0]], m2[s[:end]] = s[:end], p[0]
                    if dfs(p[1:], s[end:], m1, m2):
                        return True
                    del m1[p[0]]
                    del m2[s[:end]]
                elif p[0] in m1 and s[:end] in m2 and m1[p[0]] == s[:end] and m2[s[:end]] == p[0]:
                    if dfs(p[1:], s[end:], m1, m2):
                        return True
            return False

        return dfs(p, s, {}, {})


if __name__ == '__main__':
    s = Solution()
    print s.wordPatternMatch("abab", "redblueredblue")
    print s.wordPatternMatch("aaaa", "asdasdasdasd")
    print s.wordPatternMatch("aabb", "xyzabcxzyabc")
