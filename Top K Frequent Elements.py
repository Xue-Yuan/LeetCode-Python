#O(nlogk)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pq = []
        for ky, vl in collections.Counter(nums).items():
            if len(pq) < k:
                heapq.heappush(pq, (vl, ky))
            else:
                heapq.heappushpop(pq, (vl, ky))
        return [ky for _, ky in pq]


#O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        for num, cnt in collections.Counter(nums).items():
            bucket[len(nums)-cnt].append(num)
        return [item for sublist in bucket for item in sublist][:k]
