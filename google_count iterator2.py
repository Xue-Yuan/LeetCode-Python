#coding: utf-8


"""String Decompression，把"a2b3c4"->"aabbbcccc"
Follow Up: 输入是个Iterator，输出也是Iterator
"""


import re


def solution(s):
    return re.sub(
        '([a-z])(\d+)',
        lambda m: m.group(1)*int(m.group(2)), s
    )


def solution2(s):
    if not s:
        return ''
    ch = s[0]
    i = 1
    if i < len(s) and s[i].isdigit():
        i += 1
    num = int(s[1:i])
    return ch*num + solution2(s[i:])


print solution("a2b13c4")
print solution2("a2b3c4")


class Iterator(object):
    def __init__(self, vec):
        self.itr = iter(vec)
        self.val = 0
        self.used = True

    def peek(self):
        if not self.used:
            return self.val
        self.hasNext()
        return self.val

    def hasNext(self):
        if not self.used:
            return True
        try:
            self.val = next(self.itr)
            self.used = False
            return not self.used
        except:
            return False

    def next(self):
        self.used = True
        return self.val


class NewIteraotr(object):
    def __init__(self, itr):
        self.itr = itr
        self.times = 0
        self.val = ''

    def hasNext(self):
        while self.times == 0:
            if self.itr.hasNext():
                self.val = self.itr.next()
                num = '0'
                while self.itr.hasNext() and self.itr.peek().isdigit():
                    num += self.itr.next()
                self.times = int(num)
            else:
                break
        return bool(self.times)

    def next(self):
        self.times -= 1
        return self.val


itr = NewIteraotr(Iterator("a2b13c4"))
while itr.hasNext():
    print itr.next()
