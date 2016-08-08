class Solution:
    """Without pre-process
    """
    def _quickSort(self, nums, beg, end):
        if beg >= end:
            return
        if beg + 1 == end:
            if nums[beg] > nums[end]:
                nums[beg], nums[end] = nums[end], nums[beg]
            return
        pivot = nums[end]
        i, j = beg, end-1
        while i < j:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1
        nums[i], nums[end] = nums[end], nums[i]
        self._quickSort(nums, beg, i-1)
        self._quickSort(nums, i+1, end)

    def quickSort(self, nums):
        self._quickSort(nums, 0, len(nums)-1)


class Solution2:
    def median3(self, nums, beg, end):
        mid = (beg + end) >> 1
        if nums[beg] > nums[end]:
            nums[beg], nums[end] = nums[end], nums[beg]
        if nums[beg] > nums[mid]:
            nums[mid], nums[beg] = nums[beg], nums[mid]
        if nums[mid] < nums[end]:
            nums[mid], nums[end] = nums[end], nums[mid]
        return nums[end]

    def _quickSort(self, nums, beg, end):
        if beg >= end:
            return
        if beg + 1 == end:
            if nums[beg] > nums[end]:
                nums[beg], nums[end] = nums[end], nums[beg]
            return
        pivot = self.median3(nums, beg, end)
        i, j = beg, end
        while i < j:
            i, j = i+1, j-1
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[end] = nums[end], nums[i]
        self._quickSort(nums, beg, i-1)
        self._quickSort(nums, i+1, end)

    def quickSort(self, nums):
        self._quickSort(nums, 0, len(nums)-1)
