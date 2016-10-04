class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def dfs(s, pre, num):
            if not num:
                return True
            for i in range(1, len(num)+1):
                cur = num[:i]
                if len(cur) > 1 and cur[0] == '0':
                    break
                if int(cur) == s:
                    if dfs(int(pre)+int(cur), cur, num[i:]):
                        return True
            return False
        sz = len(num)
        for i, j in itertools.combinations(range(1, sz), 2):
            if not ((i > 1 and num[0] == '0') or (j > i+1 and num[i] == '0')):
                if dfs(int(num[:i])+int(num[i:j]), num[i:j], num[j:]):
                    return True
        return False
