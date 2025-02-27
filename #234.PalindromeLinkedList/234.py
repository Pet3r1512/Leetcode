from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        if head.next is None:
            return True
        
        if head.next.next is None and head.val != head.next.val:
            return False

        vals = []
        curr = head

        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        
        left = 0
        right = len(vals) - 1

        while left <= right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right = len(vals) - left - 1

        return True