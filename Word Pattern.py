class Solution(object):
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(s)) == len(set(t)) == len(set(zip(s, t))) and len(s) == len(t)
