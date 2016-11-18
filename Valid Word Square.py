class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        try:
            return all(
                words[row][col] == words[col][row]
                for row in range(len(words))
                for col in range(len(words[row]))
            )
        except:
            return False
