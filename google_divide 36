#coding: utf-8


"""http://www.1point3acres.com/bbs/thread-161198-1-1.html
给一个string很长很长，找一个substring能不能除36余1，
“agda4685766986579868687669686786786;?adfff7323” 有substring除36余1，
substring只能有数字，但可以很长很长，可以远大于long的范围。
"""


def solution(s):
    """Keep the remainders of the substrings ending at the previous
    position.
    """
    remainders = set([0])
    for ch in s:
        if not ch.isdigit():
            remainders = set([0])
        else:
            if any((r*10+int(ch)) % 36 == 1 for r in remainders):
                return True
            remainders = {(r*10+int(ch)) % 36 for r in remainders} | {0}
    return False


if __name__ == '__main__':
    print solution('agda4685766986579868687669686786786;?adfff7323')
    print solution('agda4;?adfff367')
