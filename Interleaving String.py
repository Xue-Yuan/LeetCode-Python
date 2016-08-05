class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1+l2 != l3:
            return False
        opt = [[False] * (l1+1) for _ in range(l2+1)]
        opt[0][0] = True

        for i1 in range(1, l1+1):
            opt[0][i1] = opt[0][i1-1] and s1[i1-1] == s3[i1-1]

        for i2 in range(1, l2+1):
            opt[i2][0] = opt[i2-1][0] and s2[i2-1] == s3[i2-1]
            for i1 in range(1, l1+1):
                opt[i2][i1] = (opt[i2-1][i1] and s2[i2-1] == s3[i2+i1-1]
                               or opt[i2][i1-1] and s1[i1-1] == s3[i2+i1-1])

        return opt[-1][-1]

#Of course we can use only O(min(l1, l2)) space
