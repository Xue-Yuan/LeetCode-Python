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


# https://scottduan.gitbooks.io/leetcode-review/content/sentence_screen_fitting.html
def wordsTyping(sentence, rows, cols):
    sentence = ' '.join(sentence) + ' '
    sz, cnt = len(sentence), 0
    m = [0] * sz
    for i in range(1, sz):
        m[i] = 1 if sentence[i] == ' ' else m[i-1]-1
    for i in range(rows):
        cnt += cols
        cnt += m[cnt % sz]
    return cnt/sz


sentence = ["I", "had"]
print Solution().wordsTyping(sentence, 1, 5)
print wordsTyping(sentence, 1, 5)
