import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans, queue = [], collections.deque()
        for idx, num in enumerate(nums):
            if queue and idx - queue[0][1] > k-1:
                queue.popleft()
            while queue and queue[-1][0] < num:
                queue.pop()
            queue.append((num, idx))
            if idx >= k-1:
                ans.append(queue[0][0])
        return ans


if __name__ == "__main__":
    print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], k=3)
