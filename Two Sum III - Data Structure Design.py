class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums = collections.defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.nums[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.nums:
            diff = value - num
            if diff in self.nums and (diff != num or self.nums[diff] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
