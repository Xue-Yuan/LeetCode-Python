def longestPalindromeSubsequence(s):
    sz = len(s)
    dp = [[0] * sz for _ in range(sz)]
    dp[0][0] = 1
    for r in range(1, sz):
        dp[r][r] = 1
        for l in range(r)[::-1]:
            if s[l] == s[r]:
                if l+1 == r:
                    dp[l][r] = 2
                else:
                    dp[l][r] = dp[l+1][r-1] + 2
            else:
                if l+1 == r:
                    dp[l][r] = 1
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
    return dp[0][sz-1]



print longestPalindromeSubsequence("GEEKSFORGEEKS")
