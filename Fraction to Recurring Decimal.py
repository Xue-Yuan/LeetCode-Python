class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if (numerator*denominator) < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        interger, remainder = divmod(numerator, denominator)
        decimal, m = '', {}
        while remainder > 0:
            if remainder in m:
                decimal = decimal[:m[remainder]]+'('+decimal[m[remainder]:]+')'
                break
            m[remainder] = len(decimal)
            quotient, remainder = divmod(remainder*10, denominator)
            decimal += str(quotient)
        if decimal:
            return sign + str(interger) + '.' + decimal
        return sign + str(interger)
