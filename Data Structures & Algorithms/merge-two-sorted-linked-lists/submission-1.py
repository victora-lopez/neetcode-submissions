# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        dummy = ListNode()
        head = dummy

        curr1, curr2 = list1, list2

        while curr1 or curr2:
            if curr1 is None:
                dummy.next = curr2
                break
            elif curr2 is None:
                dummy.next = curr1
                break
            
            val1, val2 = curr1.val, curr2.val

            if val1 <= val2:
                dummy.next = curr1
                curr1 = curr1.next
            elif val2 < val1:
                dummy.next = curr2
                curr2 = curr2.next
            dummy = dummy.next

        return head.next