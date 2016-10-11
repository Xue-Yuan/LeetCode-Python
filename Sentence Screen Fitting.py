class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        sz = len(sentence)
        total = sum(len(s)+1 for s in sentence)
        times = (cols+1)/total*rows
        cols = (cols+1) % total
        idx, r, cur, start = 0, 0, cols, 0
        cache = {}
        while r < rows:
            if cur == cols and idx in cache:
                r += 1
                times += cache[idx] < idx
                idx = cache[idx]
            else:
                if len(sentence[idx])+1 <= cur:
                    cur -= len(sentence[idx])+1
                    idx = (idx+1) % sz
                    times += idx == 0
                else:
                    start = cache[start] = idx
                    r += 1
                    cur = cols
        return times
