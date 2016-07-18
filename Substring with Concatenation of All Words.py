class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        need = Counter(words)
        w_sz, ret = len(words[0]), []
        for i in range(w_sz):
            b, found, cnt = i, Counter(), 0
            for e in range(b, len(s), w_sz):
                word = s[e: e+w_sz]
                if word in need:
                    found[word] += 1
                    cnt += 1
                    while need[word] < found[word]:
                        found[s[b: b+w_sz]] -= 1
                        b += w_sz
                        cnt -= 1
                    if cnt == len(words):
                        ret.append(b)
                else:
                    b = e + w_sz
                    found.clear()
                    cnt = 0
        return ret
