under20 = [
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
]

between20_100 = [
    "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
]

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        def _(num):
            if num < 20:
                return under20[num]
            if num < 100:
                return (between20_100[num/10] + ' ' + under20[num%10]).strip()
            if num < 1000:
                return (_(num/100) + ' Hundred ' + _(num%100)).strip()
            if num < 1000000:
                return (_(num/1000) + ' Thousand ' + _(num%1000)).strip()
            if num < 1000000000:
                return (_(num/1000000) + ' Million ' + _(num%1000000)).strip()
            return (_(num/1000000000) + ' Billion ' + _(num%1000000000)).strip()

        return _(num)
