def solution(s):
    def _dfs(s, path):
        if not s:
            if path == path[::-1]:
                return len(path)
            return 0
        ans = 0
        for idx in range(1, len(s)+1):
            path.append(s[:idx])
            ans = max(ans, _dfs(s[idx:], path))
            path.pop()
        return ans
    return _dfs(s, [])


if __name__ == '__main__':
    assert(solution('abab') == 2)
    assert(solution('teammate') == 6)
    assert(solution('ab') == 1)
    assert(solution('aaa') == 3)
    assert(solution('') == 0)
