class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1)+1, len(word2)+1
        opt = [range(l2) for _ in range(l1)]
        for r in range(1, l1):
            opt[r][0] = r
            for c in range(1, l2):
                if word1[r-1] == word2[c-1]:
                    opt[r][c] = opt[r-1][c-1]
                else:
                    opt[r][c] = min(opt[r-1][c-1], opt[r-1][c], opt[r][c-1])+1
        return opt[-1][-1]


class Solution2(object):
    def minDistance(self, word1, word2):
        """Of course we can use one rolling array
        """
        l1, l2 = len(word1)+1, len(word2)+1
        opt = range(l2)
        for r in range(1, l1):
            pre, opt[0] = opt[0], r
            for c in range(1, l2):
                _pre = opt[c]
                if word1[r-1] == word2[c-1]:
                    opt[c] = pre
                else:
                    opt[c] = min(pre, opt[c], opt[c-1])+1
                pre = _pre
        return opt[-1]
