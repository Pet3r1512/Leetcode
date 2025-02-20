# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        temp = ListNode(0, head)
        current = temp

        while current.next is not None:
            if current.val == val:
                current.next = current.next.next
            else:
                current.next = current.next
        
        return temp.next

solution_instance = Solution()
print(solution_instance.removeElements([1,2,3,6,4,5,6], 6))            