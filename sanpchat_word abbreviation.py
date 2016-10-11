class TrieNode(object):
    def __init__(self):
        self.unique = True
        self.m = {}


def insert(node, word):
    for ch in word:
        if ch in node.m:
            node.m[ch].unique = False
        else:
            node.m[ch] = TrieNode()
        node = node.m[ch]


def build_trie(words):
    word_tries = {}
    for word in words:
        abbr = word[0]+str(len(word))+word[-1]
        if abbr not in word_tries:
            word_tries[abbr] = TrieNode()
        insert(word_tries[abbr], word)
    return word_tries


def abbreviate(word_tries, words):
    ans = []
    for word in words:
        if len(word) < 4:
            ans.append(word)
        else:
            root = word_tries[word[0]+str(len(word))+word[-1]]
            for idx, ch in enumerate(word):
                root = root.m[ch]
                if root.unique:
                    tmp = word[:idx+1] + str(len(word)) + word[-1]
                    if len(tmp) >= len(word):
                        ans.append(word)
                    else:
                        ans.append(tmp)
                    break
    return ans


def solution(words):
    return abbreviate(build_trie(words), words)


if __name__ == '__main__':
    expected = ['l4e', 'god', 'internal', 'me', 'i8t', 'interval', 'inte9n', 'f4j', 'intr9n']
    result = solution(['like', 'god',  'internal', 'me' ,'internet', 'interval', 'intension', 'fthj', 'intrusion'])
    assert(expected == result)
