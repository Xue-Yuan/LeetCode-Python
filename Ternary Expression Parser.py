class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def _parse(expression):
            try:
                idx = expression.index('?')
                sum_ = 0
                for i in range(idx, len(expression)):
                    sum_ += expression[i] == '?'
                    sum_ -= expression[i] == ':'
                    if sum_ == 0:
                        break
                if _parse(expression[:idx]) == 'F':
                    return _parse(expression[i+1:])
                else:
                    return _parse(expression[idx+1:i])
            except:
                return expression
        return _parse(expression)


if __name__ == '__main__':
    s = Solution()
    print s.parseTernary("T?2:3")
    print s.parseTernary("F?1:T?4:5")
    print s.parseTernary("T?T?F:5:3")
