# Naive solution
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        idx = total = line = 0
        sz = len(sentence)
        for _ in range(rows):
            while line + 1 + len(sentence[idx]) <= cols+1:
                line += len(sentence[idx])+1
                total += idx == sz-1
                idx = (idx+1) % sz
            line = 0
        return total


class Solution2(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        sentence = ' '.join(sentence) + ' '
        sz, cnt = len(sentence), 0
        for _ in range(rows):
            cnt += cols
            if sentence[cnt % sz] == ' ':
                cnt += 1
            else:
                while cnt > 0 and sentence[(cnt-1) % sz] != ' ':
                    cnt -= 1
        return cnt / sz



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
