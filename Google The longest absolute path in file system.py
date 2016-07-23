#recursive solution
class Solution(object):

    def longest_absolute_path(self, fpth):
        files = fpth.split('\n')
        max_len, _ = self._dfs(files, 0, -1)
        return max_len

    #return len and idx. If ends with a directory, len = 0
    def _dfs(self, files, idx, lvl):
        if idx >= len(files):
            return 0, idx
        max_len = 0
        while idx < len(files):
            cur_file = files[idx]
            cur_lvl = cur_file.count('\t')
            if cur_lvl <= lvl:
                return max_len, idx
            cur_file = cur_file.lstrip('\t')
            if '.' in cur_file: # if cur_file is not a directory
                #len(cur_file)+1 for the backslash
                max_len, idx = max(max_len, len(cur_file)), idx+1
            else:
                nxt_len, idx = self._dfs(files, idx+1, cur_lvl)
                if nxt_len > 0:
                    max_len = max(max_len, len(cur_file)+nxt_len+1)
        return max_len, idx


#explicitly use a stack
class Solution2(object):

    def longest_absolute_path(self, fpth):
        files = fpth.split('\n')
        stk = [(-1, -1)]
        max_len, prev_lvl = 0, -1
        for file in files:
            cur_lvl = file.count('\t')
            file = file.lstrip('\t')
            while cur_lvl <= stk[-1][1]:
                stk.pop()
            cur_len = stk[-1][0]+len(file)+1
            if '.' in file:
                max_len = max(max_len, cur_len)
            stk.append((cur_len, cur_lvl))
        return max_len
