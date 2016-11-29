# Naive solution
class Solution1(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        row = total = cur = idx = 0
        sz = len(sentence)
        while row < rows:
            word = sentence[idx]
            if cur + len(word) + 1 <= cols + 1:
                cur += len(word) + 1
                total += (idx+1) >= sz
                idx = (idx+1) % sz
            else:
                row += 1
                cur = 0
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
