"""TLE for the last test case. Need to be modified.
"""

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """   
        if not dictionary:
            return str(len(target))

        def abbreviate(word, path, cnt, word_len):
            if not word:
                if cnt:
                    word_len += 1
                    path += str(cnt)
                yield word_len, path
            else:
                for abbr in itertools.chain(
                        (abbreviate(word[1:], path+str(cnt)+word[0], 0, word_len+2) if cnt
                         else abbreviate(word[1:], path+word[0], 0, word_len+1)),
                        abbreviate(word[1:], path, cnt+1, word_len)):
                    yield abbr

        m = {abbr for word in dictionary for _, abbr in abbreviate(word, '', 0, 0)}
        ans, ans_len = '', len(target)+1
        for l, abbr in abbreviate(target, '', 0, 0):
            if abbr not in m and l < ans_len:
                ans, ans_len = abbr, l
        return ans
