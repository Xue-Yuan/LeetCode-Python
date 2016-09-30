class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.m = collections.defaultdict(list)
        for idx, word in enumerate(words):
            self.m[word].append(idx)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.m[word1], self.m[word2]
        i1, i2, ans = 0, 0, abs(l1[0] - l2[0])
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] > l2[i2]:
                l1, l2, i1, i2 = l2, l1, i2, i1
            ans = min(ans, l2[i2] - l1[i1])
            i1 += 1
        return ans

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
