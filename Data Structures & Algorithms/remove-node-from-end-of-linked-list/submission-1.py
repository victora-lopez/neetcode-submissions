# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        first = head
        while first:
            length += 1
            first = first.next
        

        if (length - n) == 0:
            return head.next
            
        index = 1
        second = head

        while index < (length - n):
            index += 1
            second = second.next

        second.next = second.next.next

        return head
        
