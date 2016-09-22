class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(0, len(haystack)-len(needle)+1):
            for j in range(0, len(needle)):
                if i+j == len(haystack):
                    break
                elif haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return 0 if not (haystack or needle) else -1


class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hsz, nsz = len(haystack), len(needle)
        for i in range(hsz-nsz+1):
            if haystack[i:i+nsz] == needle:
                return i
        return -1


#KMP
class Solution3(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lps = [0] * len(needle)
        for i in range(1, len(needle)):
            l = lps[i-1]
            while needle[l] != needle[i] and l > 0:
                l = lps[l-1]
            lps[i] = l + (needle[i] == needle[l])
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if j > 0 and haystack[i] != needle[j]:
                j = lps[j-1]
            else:
                j += haystack[i] == needle[j]
                i += 1
        return i - j if j == len(needle) else -1
