class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp, ret = [0] * len(s), 0
        for i in range(1, len(s)):
            if s[i] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + 2
                if i-dp[i-1]-2 >= 0:
                    dp[i] += dp[i-dp[i-1]-2]
                ret = max(ret, dp[i])
        return ret


class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk, ret = [], 0
        for idx in range(len(s)):
            if s[idx] == '(':
                stk.append(idx)
            else:
                if stk and s[stk[-1]] == '(':
                    stk.pop()
                    last = stk[-1] if stk else -1
                    ret = max(ret, idx-last)
                else:
                    stk.append(idx)
        return ret
