def flip_byte(num):
    l, r = 0x80, 0x01
    dst = 7
    while l > r:
        num = ((num & l) >> dst) | ((num & r) << dst) | (num & (~l & ~r))
        l >>= 1
        r <<= 1
        dst -= 2
    return num
