#coding: utf-8


"""coding 1：编码解码。比如A是1，B是2。。。Z是26，第一问是一串字母（e.g.,ABACCC），
编码成数字
第二问是给定一串数字（e.g.,123121452），解码成所有可能的字符串，follow up是怎么
改进performance
"""


from collections import defaultdict


s = '123121452'


def dfs(i, path, ans=[]):
    if i == len(s):
        ans.append(path)
        return ans
    if s[i] != '0':
        ch = chr(int(s[i])-1+ord('A'))
        dfs(i+1, path+ch)
        if i+2 <= len(s) and '10' <= s[i:i+2] <= '26':
            ch = chr(int(s[i:i+2])-1+ord('A'))
            dfs(i+2, path+ch)
    return ans


m = defaultdict(list)
m[len(s)] = ['']
A = ord('A')


def dfs2(i):
    """Follow up
    """
    if i in m:
        return m[i]
    if s[i] != '0':
        ch = chr(int(s[i])-1+A)
        m[i] += [ch+tmp for tmp in dfs2(i+1)]
        if i+2 <= len(s) and '10' <= s[i:i+2] <= '26':
            ch = chr(int(s[i:i+2])-1+A)
            m[i] += [ch+tmp for tmp in dfs2(i+2)]
        return m[i]
    return []


print dfs(0, '')
print dfs2(0)
