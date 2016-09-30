class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pre, pos = None, -1
        same, ans = word1 == word2, len(words)
        for idx, word in enumerate(words):
            if word in (word1, word2):
                if pre and (pre != word or same):
                    ans = min(ans, idx-pos)
                pre, pos = word, idx
        return ans
