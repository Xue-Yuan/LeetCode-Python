class Solution:

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        sz = len(word)
        num = 0
        idx = 0
        for ch in abbr:
            if num == 0 and ch == '0':
                # No leading 0s
                return False
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                idx += num
                num = 0
                if idx >= sz or word[idx] != ch:
                    return False
                idx += 1
        return idx + num == sz


if __name__ == "__main__":
    s = Solution()
    print(s.validWordAbbreviation('substitution', 's10n'))
    print(s.validWordAbbreviation('substitution', 'sub4u4'))
    print(s.validWordAbbreviation('substitution', '12'))
    print(s.validWordAbbreviation('substitution', 'su3i1u2on'))
    print(s.validWordAbbreviation('substitution', 'substitution'))
    print('------------------------------')
    print(s.validWordAbbreviation('substitution', 's55n'))
    print(s.validWordAbbreviation('substitution', 's010n'))
    print(s.validWordAbbreviation('substitution', 's0ubstitution'))
