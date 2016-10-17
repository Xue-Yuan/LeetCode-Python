def solution(hills):
    sz = len(hills)
    opt = [0] * sz
    def _dfs(cur):
        if not (0 <= cur < sz):
            return 0
        if opt[cur]:
            return opt[cur]
        for idx in (cur-1, cur+1):
            if 0 <= idx < sz and hills[idx] < hills[cur]:
                opt[cur] = max(opt[cur], _dfs(idx)+1)
        for idx in (cur-2, cur+2):
            mid = (cur+idx)/2
            if 0 <= idx < sz and hills[idx] < hills[mid] < hills[cur]:
                opt[cur] = max(opt[cur], _dfs(idx)+1)
        return opt[cur]
    return max(_dfs(cur) for cur in range(sz))
