class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        (init, sign, dot, integer, decimal,
            exp, exp_sign, exp_integer, invalid) = range(9)
        state = init
        for ch in s.strip():
            if state == init:
                if ch in '-+':
                    state = sign
                elif ch == '.':
                    state = dot
                elif ch.isdigit():
                    state = integer
                else:
                    state = invalid
            elif state == sign:
                if ch == '.':
                    state = dot
                elif ch.isdigit():
                    state = integer
                else:
                    state = invalid
            elif state == integer:
                if ch.isdigit():
                    continue
                elif ch == '.':
                    state = decimal
                elif ch in 'eE':
                    state = exp
                else:
                    state = invalid
            elif state == dot:
                if ch.isdigit():
                    state = decimal
                else:
                    state = invalid
            elif state == decimal:
                if ch.isdigit():
                    continue
                elif ch == '.':
                    state = invalid
                elif ch in 'eE':
                    state = exp
                else:
                    state = invalid
            elif state == exp:
                if ch in '-+':
                    state = exp_sign
                elif ch.isdigit():
                    state = exp_integer
                else:
                    state = invalid
            elif state == exp_sign:
                if ch.isdigit():
                    state = exp_integer
                else:
                    state = invalid
            elif state == exp_integer:
                if ch.isdigit():
                    continue
                else:
                    state = invalid
            elif state == invalid:
                break
            else:
                state = invalid
        return state in (integer, decimal, exp_integer)


if __name__ == '__main__':
    solution = Solution()
    assert(solution.isNumber('1 '))
    assert(solution.isNumber('123'))
    assert(solution.isNumber('1.'))
    assert(solution.isNumber('.1'))
    assert(solution.isNumber('1.e1'))
    assert(solution.isNumber('-1.e1'))
    assert(solution.isNumber('-.1e2'))
    assert(not solution.isNumber('0..'))
    assert(not solution.isNumber('e'))
    assert(not solution.isNumber('1e1.'))
