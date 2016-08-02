class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        import collections
        m = collections.defaultdict(list)
        for s in strs:
            m[tuple(sorted(s))].append(s)
        return m.values()
