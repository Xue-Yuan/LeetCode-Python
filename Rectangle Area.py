class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        l = max(A, E)
        b = max(B, F)
        r = min(C, G)
        t = min(D, H)
        overlap = (r-l)*(t-b) if r > l and t > b else 0
        return (C-A)*(D-B) + (G-E)*(H-F) - overlap
