#coding: utf-8

"""有一个本地存储log的系统，capacity 为n,现在有m个消息源，发送消息给系统
class log{ String msg, String address}。寻找一个threshold，当一个消
息源消息数目<=bound的时候，接受全部消息，大于bound时候截取bound个存储，
输入是list<Log>要求选择bound最大化利用存储容量
举了个例子。[10, 20, 20, 50, 70] 存储容量90.bound就是20
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


def findBound(nums, capacity):
    def find(b, e, capacity, pre):
        if b > e:
            return pre
        if b == e:
            if nums[b] > capacity:
                return pre
            else:
                return nums[b]
        m = (b+e) >> 1
        quickselect(nums, b, e, m)
        less = sum(nums[b:m+1])
        greater = nums[m] * (len(nums)-m)
        if less+greater < capacity:
            return find(m+1, e, capacity-less, nums[m])
        else:
            return find(b, m-1, capacity, pre)
    bound = find(0, len(nums)-1, capacity, float(capacity)/len(nums))
    less = [num for num in nums if num <= bound]
    return bound + float(capacity-sum(less)-bound*(len(nums)-len(less))) / (len(nums)-len(less))


if __name__ == '__main__':
    print findBound([20, 50], 30)
    print findBound([20, 40, 100], 70)
    print findBound([70, 20, 30, 40, 60], 50)
