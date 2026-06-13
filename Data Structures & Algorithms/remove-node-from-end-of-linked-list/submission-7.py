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
        
        removeIndex = length - n

        if removeIndex == 0:
            return head.next

        first = head
        for i in range(length - 1):
            if i + 1 == removeIndex:
                first.next = first.next.next
                break
            first = first.next

        return head
        
