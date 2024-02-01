# Definition for singly-linked list.
from typing import Optional, TypeVar

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a result as a ListNode
        result = ListNode() 
        currentNode = result
        carry = 0

        while l1 or l2 or carry: #get each node for each ListNode
            # get current node's value
            # if that value is none then use 0 instead
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x + y + carry

            # if the sum is 10 then only take 0 for the result 
            digit = sum % 10
            carry = sum // 10

            currentNode.next = ListNode(digit) #put that result to ListNode
            currentNode = currentNode.next

            # move to next digit of 2 ListNode
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        #  Make sure the result is the head of ListNode
        return result.next

