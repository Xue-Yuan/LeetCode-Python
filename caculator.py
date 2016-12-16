import operator


m = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
}


def caculate(exp):
    def is_higher(op1, op2):
        """Return true when op1 is of higher or the same priority
        """
        if op1 in '()' or op2 in '()':
            return False
        return op1 in '*/' or op2 in '+-'

    def _cal(ops, nums):
        if not ops or not nums:
            return
        tmp_op = ops.pop()
        n2 = nums.pop()
        n1 = nums.pop()
        nums.append(m[tmp_op](n1, n2))

    ops, nums = [], []
    num = ''
    for ch in exp + ' ':
        if ch.isdigit():
            num += ch
        else:
            if num:
                nums.append(int(num))
                num = ''
            # print nums, ops
            if ch == '(':
                ops.append(ch)
            elif ch in '+-*/':
                if not ops or ops[-1] == '(':
                    ops.append(ch)
                else:
                    while ops and is_higher(ops[-1], ch):
                        _cal(ops, nums)
                    ops.append(ch)
            elif ch == ')':
                while ops and ops[-1] != '(':
                    _cal(ops, nums)
                ops.pop()
    while ops:
        # print nums, ops
        _cal(ops, nums)
    return nums[-1]


if __name__ == '__main__':
    while True:
        exp = raw_input("Enter expression: ")
        print 'expected: {}, got: {}'.format(eval(exp), caculate(exp))
