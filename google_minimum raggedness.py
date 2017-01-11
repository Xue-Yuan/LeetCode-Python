def diff(words, i, j, m, memo={}):
    if (i, j) not in memo:
        total = sum(len(word)+1 for word in words[i-1:j])
        memo[i, j] = m+1 - total
    return memo[i, j]


def minRaggedness(words, m):
    sz = len(words)
    dp = [float('inf') for _ in range(sz+1)]
    dp[0] = 0
    for i in range(1, sz+1):
        for j in range(1, i+1)[::-1]:
            d = diff(words, j, i, m)
            if d < 0:
                break
            dp[i] = min(dp[j-1]+d*d, dp[i])
    return dp[-1]


if __name__ == '__main__':
    words = ['www', 'bb', 'cc', 'fffff']
    print(minRaggedness(words, 6))
