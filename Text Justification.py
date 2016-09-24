class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line, ans, letters = [], [], 0
        for word in words:
            if letters + len(line) + len(word) > maxWidth:
                if len(line) == 1:
                    ans.append(line[0].ljust(maxWidth, ' '))
                else:
                    spaces = maxWidth - letters
                    for i in range(spaces):
                        line[i % (len(line)-1)] += ' '
                    ans.append(''.join(line))
                line[:] = []
                letters = 0
            line.append(word)
            letters += len(word)
        ans.append(' '.join(line).ljust(maxWidth, ' '))
        return ans
