from typing import List
import math


class Solution:

    def ipToCider(self, ip: str, n: int) -> List[str]:
        num = 0
        for block in ip.split('.'):
            num = (num << 8) + int(block)

        res = []
        while n > 0:
            # least significant bit (lsb).
            # We can have the {lsb} number of IPs by using bits after lsb.
            # e.g., say lsb = b'100', then we can have 4 IPs in [100, 111].
            covered = num & (-num)
            while (covered >> 1) >= n:
                covered >>= 1
            res.append(self.numToCIDR(num, covered))
            num += covered
            n -= covered
        return res

    def numToCIDR(self, num: int, covered: int) -> str:
        block = [0] * 4
        for i in range(4):
            block[i] = num % 256
            num >>= 8

        fixed_bits = 32 - int(math.log2(covered))
        return f"{block[3]}.{block[2]}.{block[1]}.{block[0]}/{fixed_bits}"


if __name__ == '__main__':
    s = Solution()
    print(s.ipToCider("255.0.0.7", 10))
