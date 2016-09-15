class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min(
            abs(a-b)
            for a in [i for i in words if words[i] == word1]
            for b in [j for j in words if words[j] == word2]
        )
