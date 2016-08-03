class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for idx, num in enumerate(reversed(digits)):
            sum = num + carry
            carry, digits[~idx] = sum / 10, sum % 10
        return [carry] + digits if carry else digits
