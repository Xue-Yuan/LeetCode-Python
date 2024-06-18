from typing import List, Tuple
import random


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1, target)

    def quickSelect(self, nums: List[int], low: int, high: int,
                    target: int) -> int:
        b, e = self.partition(nums, low, high)
        if b <= target <= e:
            return nums[target]
        if e < target:
            return self.quickSelect(nums, e + 1, high, target)
        else:
            return self.quickSelect(nums, low, b - 1, target)

    def partition(self, items: List[int], low: int,
                  high: int) -> Tuple[int, int]:
        # Choose a random pivot to improve performance
        p = random.randint(low, high)
        items[p], items[high] = items[high], items[p]
        pivot = items[high]
        i = low

        for j in range(low, high):
            if items[j] < pivot:
                items[i], items[j] = items[j], items[i]
                i += 1

        # Move values equal to pivot together in the middle. Otherwise
        # fail the last test case where a huge amount of same values packed
        # in the middle.
        start = -1
        for j in range(i, high):
            if items[j] == pivot:
                start = start if start >= 0 else j
                items[i], items[j] = items[j], items[i]
                i += 1
        items[i], items[high] = items[high], items[i]
        return (start, i) if start >= 0 else (i, i)


class Solution2:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Same idea, but uses more space
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        if len(left) + len(middle) >= k > len(left):
            return middle[0]
        if k <= len(left):
            return self.findKthLargest(left, k)
        return self.findKthLargest(right, k - len(left) - len(middle))


class Solution3:
    '''Basic version of solution1 without optimization. Fails the online judge.
    '''

    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        return self.quickSelect(nums, 0, len(nums) - 1, target)

    def quickSelect(self, nums: List[int], low: int, high: int,
                    target: int) -> int:
        pivot = self.partition(nums, low, high)
        if target == pivot:
            return nums[target]
        if pivot < target:
            return self.quickSelect(nums, pivot + 1, high, target)
        else:
            return self.quickSelect(nums, low, pivot - 1, target)

    def partition(self, items: List[int], low: int, high: int) -> int:
        # Choose a random pivot to improve performance
        p = random.randint(low, high)
        items[p], items[high] = items[high], items[p]
        pivot = items[high]
        i = low

        for j in range(low, high):
            if items[j] <= pivot:
                items[i], items[j] = items[j], items[i]
                i += 1
        items[i], items[high] = items[high], items[i]

        return i
