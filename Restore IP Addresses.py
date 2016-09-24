class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def _dfs(s, path, ret=[]):
            if not s and len(path) == 4:
                ret.append('.'.join(path))
                return ret
            if len(path) < 4:
                for i in range(1, min(4, len(s)+1)):
                    tmp = s[:i]
                    if 0 <= int(tmp) <= 255 and (len(tmp) == 1 or tmp.lstrip('0') == tmp):
                        path.append(tmp)
                        _dfs(s[i:], path)
                        path.pop()
            return ret
        return _dfs(s, [])


if __name__ == '__main__':
    solution = Solution()
    print solution.restoreIpAddresses('0000')
    print solution.restoreIpAddresses('25525511135')
