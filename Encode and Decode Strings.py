class Codec(object):
    def encode(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Use header.
        ans = ''
        for s in strs:
            ans += str(len(s)) + '#' + s
        return ans

    def decode(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        idx = 0
        while idx < len(s):
            end = s.find('#', idx)
            lnth = int(s[idx:end])
            ans.append(s[end+1: end+1+lnth])
            idx = end+lnth+1
        return ans

if __name__ == "__main__":
    strs = ['hello', 'this', 'is', 'a', 'test', '!']
    Cd = Codec()
    print Cd.decode(Cd.encode(strs))
    print Cd.decode(Cd.encode([]))
