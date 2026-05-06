# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# i want to combine the lists into one list that is organized
# in non-decreasing order.
#
# the best way to go about this is to traverse both lists at the same time
# and compare the value of the node i am on in both lists to each other
# if the value of the node i am on in list 1 is larger then i will
# add that to the new list i made and move on to the next node in list1
# if the node value of list2 is bigger then i append/point to that node
# in the new list made and move on to the next node in list 2
#
# once one of the lists is fully traversed, we need to test if there
# were any left over values in the other list, and if there were
# then we point the created list to it so it will have the remaining 
# values

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next




