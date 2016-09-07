#https://discuss.leetcode.com/topic/17409/6-lines-general-case-o-n-time-and-o-k-space


def majorityElement(nums, k):
    cntr = collections.Counter()
    for num in nums:
        cntr[num] += 1
        if len(cntr) > k:
            #Down vote all element once
            cntr -= collections.Counter(set(cntr))
    cntr = collections.Counter(n for n in nums if n in cntr)
    return [n for n in cntr if cntr[n] > len(nums)/k]
