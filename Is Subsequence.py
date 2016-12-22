import collections
import string


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0
        for ch in s:
            idx = t.find(ch, idx)
            if idx < 0:
                return False
            idx += 1
        return True


# Follow-up question. O(len(target) + sum(len(str) for str in strs))
def solution(strs, target):
    m = collections.defaultdict(list)
    for s in strs:
        if s:
            m[s[0]].append((s, 0))
    ans = []
    for ch in target:
        if ch not in m:
            continue
        tmp = []
        for s, i in m[ch]:
            i += 1
            if i < len(s):
                if s[i] == ch:
                    tmp.append((s, i))
                else:
                    m[s[i]].append((s, i))
            else:
                ans.append(s)
        m[ch] = tmp
    return ans


if __name__ == "__main__":
    strs = ["aef", "cdu", "xue", "imnqtuxy"]
    target = string.lowercase
    print solution(strs, target)
