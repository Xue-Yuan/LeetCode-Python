"""We can also make a state interface and implement different states to it,
which would make the decision tree looks prettier. And it would also be
entendable.
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = 'init'
        for ch in s.strip():
            if state == 'init':
                if ch in '-+':
                    state = 'sign'
                elif ch == '.':
                    state = 'dot'
                elif ch.isdigit():
                    state = 'number'
                else:
                    state = 'invalid'
            elif state == 'sign':
                if ch == '.':
                    state = 'dot'
                elif ch.isdigit():
                    state = 'number'
                else:
                    state = 'invalid'
            elif state == 'number':
                if ch.isdigit():
                    continue
                elif ch == '.':
                    state = 'dot_with_number'
                elif ch in 'eE':
                    state = 'exp'
                else:
                    state = 'invalid'
            elif state == 'dot':
                if ch.isdigit():
                    state = 'dot_with_number'
                else:
                    state = 'invalid'
            elif state == 'dot_with_number':
                if ch.isdigit():
                    continue
                elif ch == '.':
                    state = 'invalid'
                elif ch in 'eE':
                    state = 'exp'
                else:
                    state = 'invalid'
            elif state == 'exp':
                if ch in '-+':
                    state = 'sign_exp'
                elif ch.isdigit():
                    state = 'number_exp'
                else:
                    state = 'invalid'
            elif state == 'sign_exp':
                if ch.isdigit():
                    state = 'number_exp'
                else:
                    state = 'invalid'
            elif state == 'number_exp':
                if ch.isdigit():
                    continue
                else:
                    state = 'invalid'
            elif state == 'invalid':
                return False
            else:
                state = 'invalid'
        return state in ('number', 'dot_with_number', 'number_exp')


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
