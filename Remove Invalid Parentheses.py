class Solution(object):
    """As much as I love the solution, it cannot get rid of duplicates
    without relying on dictionary.
    """

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isValid(s):
            cnt = 0
            for ch in s:
                cnt += ch == '('
                cnt -= ch == ')'
                if cnt < 0:
                    return False
            return cnt == 0

        lvl = {s}
        while lvl:
            valid = list(filter(isValid, lvl))
            if valid:
                return valid
            lvl = {
                s[:i] + s[i + 1:]
                for s in lvl
                for i in range(len(s)) if s[i] in '()'
            }
        return []


class Solution2:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []

        def remove(s: str, last_checked_idx: int, last_removed_idx: int,
                   open: str, close: str):
            open_cnt = close_cnt = 0
            for i in range(last_checked_idx, len(s)):
                if s[i] == open:
                    open_cnt += 1
                if s[i] == close:
                    close_cnt += 1
                if open_cnt >= close_cnt:
                    continue
                for j in range(last_removed_idx, i + 1):
                    if (s[j] == close
                            and (j == last_removed_idx or s[j] != s[j - 1])):
                        remove(s[:j] + s[j + 1:], i, j, open, close)
                return
            r = s[::-1]
            if open == "(":
                remove(r, 0, 0, ")", "(")
            else:
                ans.append(r)

        remove(s, 0, 0, "(", ")")
        return ans
