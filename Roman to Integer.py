letters = {
    '': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)-1):
            if letters[s[i]] < letters[s[i+1]]:
                total -= letters[s[i]]
            else:
                total += letters[s[i]]
        total += letters[s[-1]]
        return total
