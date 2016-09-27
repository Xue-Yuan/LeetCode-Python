class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m1, m2 = {}, {}
        for idx, (c1, c2) in enumerate(zip(s, t)):
            if m1.get(c1, -1) != m2.get(c2, -1):
                return False
            m1[c1] = m2[c2] = idx
        return True
