class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_and_sort_circular_linked_list(head: ListNode,
                                         insertVal: int) -> ListNode:
    new_node = ListNode(insertVal)

    if not head:
        new_node.next = new_node
        return new_node

    pre = head
    cur = head.next
    while cur != head:
        if (pre.val <= insert_val <= cur.val
                or pre.val > cur.val and insert_val >= pre.val
                or insert_val <= cur.val):
            break
        pre = cur
        cur = cur.next

    pre.next = new_node
    new_node.next = cur

    return head


def print_circular_linked_list(head: ListNode):
    if not head:
        print("List is empty")
        return

    current = head
    while True:
        print(current.val, end=" -> ")
        current = current.next
        if current == head:
            break
    print("(head)")


if __name__ == "__main__":
    # Example usage:
    head = ListNode(3)
    second = ListNode(4)
    third = ListNode(1)
    head.next = second
    second.next = third
    third.next = head

    print("Original list:")
    print_circular_linked_list(head)

    insert_val = 5
    head = insert_and_sort_circular_linked_list(head, insert_val)

    print("List after insertion and sort:")
    print_circular_linked_list(head)
