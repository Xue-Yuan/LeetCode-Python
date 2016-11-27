"""insert the minimum number of characters to transform the input string
to a palimdrome string. Return the number of characters need to be inserted
"""


def minimun_insert(s):
    sz = len(s)
    opt = [[0] * sz for _ in range(sz)]
    for i in range(sz)[::-1]:
        opt[i][i] = 0
        for j in range(i+1, sz):
            opt[i][j] = float('inf')
            if s[i] == s[j]:
                opt[i][j] = opt[i+1][j-1]
            else:
                opt[i][j] = min(opt[i+1][j], opt[i][j-1])+1
    return opt[0][sz-1]
