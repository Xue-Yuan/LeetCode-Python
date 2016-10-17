class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = collections.defaultdict(list)
        for s in strs:
            m[''.join(sorted(s))].append(s)
        return m.values()
