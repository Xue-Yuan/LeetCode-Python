_thousands = ["", "Thousand", "Million", "Billion", "Trillion"]
_ones = [
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
]
_tens = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    1: "Ten",
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}


class Solution:

    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"

        def lessThanThousand(num: int) -> str:
            if num < 10:
                return _ones[num]
            if 10 <= num < 20:
                return _tens[num]
            if 20 <= num < 100:
                return f"{_tens[num//10]} {_ones[num%10]}".strip()
            hundred = num // 100
            tens = lessThanThousand(num % 100)
            return f"{_ones[hundred]} Hundred {tens}".strip()

        ans = []
        thousand_cnt = 0
        while num:
            h = num % 1000
            if h:
                if thousand_cnt:
                    ans.append(_thousands[thousand_cnt])
                ans.append(lessThanThousand(h))
            num //= 1000
            thousand_cnt += 1
        return " ".join(reversed(ans))
