def sulution(a, b):
    if b:
        tmp, cnt = b & -b, 0
        while tmp:
            cnt += 1
            tmp >>= 1
        return (a << (cnt-1)) + sulution(a, b & (b-1))
    return 0

print sulution(2, 3)
print sulution(23, 3)
print sulution(3, 23)
print 79 * 56, sulution(79, 56)
