from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = head
        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next
        return head

solution = Solution()
print(solution.deleteDuplicates([1,1,2]))
     