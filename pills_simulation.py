#coding: utf-8

"""白人小哥，看起来就智商很高的那种。题目是给一瓶药，里面100颗完整的药片,
每天需要吃半颗。每天吃的方法是随机从瓶子里取一颗药，如果是整颗就吃半颗,
剩下半颗扔回瓶子里；如果取出的是半颗，那就直接吃掉。第一小问是simulate这个过程,
然后print每天瓶中剩下的整颗和半颗的数量，直到空瓶。第二问是，求整个simulation
过程中，瓶中剩下1整颗，0半颗的概率。最后问了running time。
"""

m = {(1, 0): 1, (0, 0): 0}


def dfs(w, h):
    if w < 0 or h < 0:
        return 0
    if (w, h) in m:
        return m[w, h]
    l, r = float(w)/(w+h), float(h)/(w+h)
    m[w, h] = dfs(w-1, h+1)*l + dfs(w, h-1)*r
    return m[w, h]


if __name__ == '__main__':
    print dfs(100, 0)
