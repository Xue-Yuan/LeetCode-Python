#coding: utf-8


"""input是两个string，例如："google", "algorithm"
output是一个string，按above例子就是："lggooe" 
"""


from collections import Counter


def solution(s, p):
    ans, cntr = '', Counter(s)
    for ch in p:
        if ch in cntr:
            ans += ch * cntr[ch]
            del cntr[ch]
    ans += ''.join(cntr.elements())
    return ans


print solution('google', 'algorithm')
