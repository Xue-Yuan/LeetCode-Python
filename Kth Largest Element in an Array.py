class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickselect(nums, b, e, k):
            if b > e:
                return
            i, j = b-1, e
            while i < j:
                i, j = i+1, j-1
                while nums[j] > nums[e]:
                    j -= 1
                while nums[i] < nums[e]:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if nums[i] > nums[e]:
                nums[i], nums[e] = nums[e], nums[i]
            if k-1 == i:
                return nums[i]
            elif k-1 > i:
                return quickselect(nums, i+1, e, k)
            else:
                return quickselect(nums, b, i-1, k)

        return quickselect(nums, 0, len(nums)-1, len(nums)-k+1)


# A huge difference with partition
class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def median3(nums, b, e):
            m = (b+e) >> 1
            if nums[b] > nums[e]:
                nums[b], nums[e] = nums[e], nums[b]
            if nums[b] > nums[m]:
                nums[b], nums[m] = nums[m], nums[b]
            if nums[m] < nums[e]:
                nums[m], nums[e] = nums[e], nums[m]
            return nums[e]

        def quickselect(nums, b, e, k):
            if b >= e:
                return nums[k-1]
            if b+1 == e:
                if nums[b] > nums[e]:
                    nums[b], nums[e] = nums[e], nums[b]
                return nums[k-1]
            pivot = median3(nums, b, e)
            i, j = b, e
            while i < j:
                i, j = i+1, j-1
                while nums[j] > pivot:
                    j -= 1
                while nums[i] < pivot:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[e] = nums[e], nums[i]
            if k-1 == i:
                return nums[i]
            elif k-1 > i:
                return quickselect(nums, i+1, e, k)
            else:
                return quickselect(nums, b, i-1, k)

        return quickselect(nums, 0, len(nums)-1, len(nums)-k+1)
