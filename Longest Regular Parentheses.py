"""http://poj.org/problem?id=2955
If consecutive sequences are not required, the problem is the same
as `combine stones`
"""
def longestRegularParentheses(s):
    sz = len(s)
    dp = [[0] * (sz+1) for _ in range(sz+1)]
    for i in range(sz, -1, -1):
        for j in range(i+1, sz+1):
            if (s[i-1] == '(' and s[j-1] == ')'
                    or s[i-1] == '[' and s[j-1] == ']'):
                dp[i][j] = dp[i+1][j-1] + 2
            # for k in range(i+1, j):
            #     dp[i][j] = max(dp[i][j], dp[i][k]+dp[k+1][j])
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[1][sz]


if __name__ == '__main__':
    print longestRegularParentheses('([][][)[()[')
    print longestRegularParentheses('((()))')
    print longestRegularParentheses('()()()')
    print longestRegularParentheses('([]])')
    print longestRegularParentheses(')[)(')
    print longestRegularParentheses('([][][)')
