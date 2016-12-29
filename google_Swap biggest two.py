class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def printList(head):
    if not head:
        return
    print head.val,
    printList(head.next)


def swap2(head):
    pre = dummy = Node(0)
    dummy.next = head
    pre1 = pre2 = None
    while pre.next:
        if not pre1:
            pre1 = pre
        elif not pre2:
            pre2 = pre
        else:
            if pre.next.val > min(pre1.next.val, pre2.next.val):
                if pre1.next.val < pre2.next.val:
                    pre1, pre2 = pre2, pre
                else:
                    pre2 = pre
        pre = pre.next
    if pre1 and pre2:
        max1, max2 = pre1.next, pre2.next
        if pre1.next != pre2:
            max1.next, max2.next = max2.next, max1.next
            pre1.next, pre2.next = pre2.next, pre1.next
        else:
            pre1.next = max2
            max1.next, max2.next = max2.next, max1
    return dummy.next


if __name__ == "__main__":
    cur = head = Node(0)
    cur.next = Node(2); cur = cur.next
    cur.next = Node(1); cur = cur.next
    cur.next = Node(3); cur = cur.next
    printList(head)
    print
    head = swap2(head)
    printList(head)
    print

    cur = head = Node(0)
    cur.next = Node(1); cur = cur.next
    cur.next = Node(3); cur = cur.next
    printList(head)
    print
    head = swap2(head)
    printList(head)
    print

    cur = head = Node(0)
    cur.next = Node(1); cur = cur.next
    printList(head)
    print
    head = swap2(head)
    printList(head)
    print

