class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        idx, num, sz = 0, 0, len(word)
        for ch in abbr:
            if ch.isdigit():
                if num == 0 and ch == '0':
                    break
                num = num*10 + int(ch)
            else:
                idx, num = idx+num, 0
                if not ((idx < sz and word[idx] == ch) or idx == sz):
                    break
                idx += 1
        return (idx+num) == sz
