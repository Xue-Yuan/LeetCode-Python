def find_binary_stream(n):
    stk = [('0' * n, False)]
    visited = set()
    visited.add('0' * n)
    while stk:
        cur, returned = stk.pop()
        visited.add(cur[-n:])
        if len(cur) == n + 2 ** n - 1:
            return cur
        if returned:
            visited.remove(cur[-n:])
        else:
            stk.append((cur, True))
            for i in '01':
                temp_string = cur + i
                if temp_string[-n:] not in visited:
                    stk.append((temp_string, False))
    return ''
