# Problem Description:

# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

# Examples:

# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.


class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def dfs(p, s, m1={}, m2={}):
            if not (s and p):
                return not (s or p)
            for i in range(1, len(s)+2-len(p)):
                _p, _s = p[0], s[:i]
                if _p not in m1 and _s not in m2:
                    m1[_p], m2[_s] = _s, _p
                    if dfs(p[1:], s[i:]):
                        return True
                    del m1[_p], m2[_s]
                elif _p in m1 and _s in m2 and m1[_p] == _s and m2[_s] == _p:
                    if dfs(p[1:], s[i:]):
                        return True
            return False
        return dfs(pattern, str)


if __name__ == '__main__':
    s = Solution()
    print s.wordPatternMatch("abab", "redblueredblue")
    print s.wordPatternMatch("aaaa", "asdasdasdasd")
    print s.wordPatternMatch("aabb", "xyzabcxzyabc")
