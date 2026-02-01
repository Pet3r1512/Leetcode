from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        tail = result

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return result.next


def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


solution = Solution()

l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])
result = solution.mergeTwoLists(l1, l2)
print_linked_list(result)

l1 = build_linked_list([])
l2 = build_linked_list([])
result = solution.mergeTwoLists(l1, l2)
print_linked_list(result)

l1 = build_linked_list([])
l2 = build_linked_list([0])
result = solution.mergeTwoLists(l1, l2)
print_linked_list(result)
