class Solution(object):
    """As long as I love the solution, it cannot get rid of duplicates
    without relying on dictionary.
    """
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            cnt = 0
            for ch in s:
                cnt += ch == '('
                cnt -= ch == ')'
                if cnt < 0:
                    return False
            return cnt == 0
        lvl = {s}
        while lvl:
            valid = filter(is_valid, lvl)
            if valid:
                return valid
            lvl = {
                s[:i] + s[i+1:] for s in lvl
                for i in range(len(s))
                if i == 0 or s[i] != s[i-1]
            }
        return []


class Solution2(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = right = 0
        for ch in s:
            left += ch == '('
            if left == 0:
                right += ch == ')'
            else:
                left -= ch == ')'

        def dfs(s, beg, left, right, ans=[]):
            if left == right == 0:
                if self.is_valid(s):
                    ans.append(s)
                return ans
            for i in range(beg, len(s)):
                if i == 0 or s[i] != s[i-1]:
                    if left > 0 and s[i] == '(':
                        dfs(s[:i]+s[i+1:], i, left-1, right)
                    if right > 0 and s[i] == ')':
                        dfs(s[:i]+s[i+1:], i, left, right-1)
            return ans

        return dfs(s, 0, left, right)

    def is_valid(self, s):
        cnt = 0
        for ch in s:
            cnt += ch == '('
            cnt -= ch == ')'
            if cnt < 0:
                return False
        return cnt == 0
