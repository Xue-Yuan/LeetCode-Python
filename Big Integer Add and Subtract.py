class bigInteger(object):
    def __init__(self, val):
        self.val = val if val else '0'

    def __neg__(self):
        if self.val and self.val[0] == '-':
            self.val = self.val[1:]
        else:
            self.val = '-' + self.val
        return self

    def __repr__(self):
        return self.val

    def __add__(self, other):
        if self.nonNegative() and other.nonNegative():
            val1, val2 = self.val, other.val
            idx1, idx2 = len(val1)-1, len(val2)-1
            ans, carry = [], 0
            while idx1 >= 0 or idx2 >= 0:
                total = carry
                if idx1 >= 0:
                    total += int(val1[idx1])
                    idx1 -= 1
                if idx2 >= 0:
                    total += int(val2[idx2])
                    idx2 -= 1
                ans.append(total % 10)
                carry = total / 10
            if carry:
                ans.append(carry)
            return bigInteger(''.join(map(str, ans[::-1])))
        elif self.nonNegative() and not other.nonNegative():
            return self - (-other)
        elif not self.nonNegative() and other.nonNegative():
            return other - (-self)
        else:
            return -(-self + (-other))

    def __sub__(self, other):
        if self.nonNegative() and other.nonNegative():
            if len(self.val) == len(other.val) and self.val < other.val:
                return -(other - self)
            elif len(self.val) < len(other.val):
                return -(other - self)
            else:
                val1, val2 = self.val, other.val
                idx1, idx2 = len(val1)-1, len(val2)-1
                ans, carry = [], 0
                while idx1 >= 0:
                    new_carry = 0
                    total_to_sub = carry + (int(val2[idx2]) if idx2 >= 0 else 0)
                    if int(val1[idx1]) < total_to_sub:
                        new_carry = 1
                    ans.append(new_carry*10+int(val1[idx1])-total_to_sub)
                    carry = new_carry
                    if idx2 >= 0:
                        idx2 -= 1
                    idx1 -= 1
                if ans[-1] == 0 and len(ans) > 1:
                    ans.pop()
                return bigInteger(''.join(map(str, ans[::-1])))
        elif self.nonNegative() and not other.nonNegative():
            return self + (-other)
        elif not self.nonNegative() and other.nonNegative():
            return -(-self + other)
        else:
            return -other - (-self)

    def nonNegative(self):
        return self.val[0] != '-'


if __name__ == '__main__':
    print bigInteger('1') - bigInteger('-2')
    print bigInteger('1') - bigInteger('2')
    print bigInteger('678') - bigInteger('789')
    print -bigInteger('-678') - bigInteger('789')
    print bigInteger('10000') - bigInteger('1')
    print bigInteger('10') - bigInteger('100')
    print bigInteger('1') - bigInteger('1')
    print bigInteger('7823451') - bigInteger('18374')
    print bigInteger('18374') - bigInteger('7823451')
