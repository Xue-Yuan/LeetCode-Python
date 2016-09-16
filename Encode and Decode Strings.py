class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        return ''.join(str(len(s))+'#'+s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        ans, idx = [], 0
        while idx < len(s):
            nxt = s.find('#', idx)
            l = int(s[idx:nxt])
            ans += s[nxt+1:nxt+1+l],
            idx = nxt+1+l
        return ans

if __name__ == '__main__':
    strs = ["i", ""]
    codec = Codec()
    print codec.decode(codec.encode(strs))
