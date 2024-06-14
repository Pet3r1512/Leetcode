# Definition for singly-linked list.
from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.nexts
    def addToList(self, newData):
        newNode = ListNode(newData)
        if self.head is None:
            self.head = newNode
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = newNode
1
def mergeLists(list1: ListNode, list2: ListNode):
    dummyNode = ListNode(0)

    tail = dummyNode
    while True:
        if list1.head is None:
            tail.next = list2.head
            break
        if list2.head is None:
            tail.next = list1.head
            break
        if list1.head <= list2.head.val:
            tail.next = list1.head
            list1.head = list1.head.next
        else:
            tail.next = list2.head
            list2.head = list2.head.next

        tail = tail.next
    return dummyNode.next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         newList = mergeLists(list1, list2)
#         print(newList)

listA = LinkedList()
listB = LinkedList()
 
# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)
 
listB.addToList(2)
listB.addToList(3)
listB.addToList(20)
listA.head = mergeLists(listA.head, listB.head)
print("Merged Linked List is:")
listA.printList()