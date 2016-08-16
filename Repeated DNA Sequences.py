class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans, record = [], collections.defaultdict(int)
        for idx in range(len(s)-9):
            sequence = s[idx:idx+10]
            if record[sequence] == 1:
                ans.append(sequence)
            record[sequence] += 1
        return ans
