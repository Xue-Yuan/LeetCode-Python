#coding: utf-8


"""一个int，比如2，转换为bit，前面都是0，只有后面最后两位有个1和0（0000.......00010）
表示是2，所以前面那些0占的空间就很浪费。小哥要设计一个protocol（写两个function，
一个serialize，一个deserialize），给一个int，然后把这个int转换成另外一种形式，
这种形式是一个List<Byte>，Byte总共8位，第一位是0/1，用作flag表示后面还有没有后续
的Byte，剩余7位是这个数字记得值。比如输入是2，输出就是一个list<Byte>，里面只包含
1个Byte，这个Byte从头到尾是 0|0000010。如果输入是个很大的数(比如他转换为32位是
0000..000001000001000000000)，那输出就是list<Byte>，里面包含多个Byte，头几个
Byte可能是1|0000000， 1|0000100，最后一个是0|0000010.
"""


def serialize(num):
    bits = 25
    mask = 0x7F << bits
    flag = 0x80
    ans = []
    while num:
        cur = (num & mask) >> bits
        num &= ~mask
        if cur:
            if num:
                cur |= flag
            ans.append(cur)
        mask >>= 7
        bits = max(bits-7, 0)
    return ans


def deserialize(vec):
    flag = 0x80
    ans = 0
    for num in vec:
        if num & flag:
            ans = (ans << 7) + (num & ~flag)
        else:
            ans = (ans << 4) + (num & ~flag)
            break
    return ans


if __name__ == '__main__':
    print(deserialize(serialize(2)))
    print(deserialize(serialize(312)))
    print(deserialize(serialize(123456789)))
