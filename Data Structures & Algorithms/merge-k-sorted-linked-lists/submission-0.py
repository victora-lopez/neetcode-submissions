# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we can merge two linked lists at a time and then once those
        # list are merged we can take that merged list and then sort
        # with the next linked list in the array
        for i in range(len(lists) - 1):
            node = head = ListNode()
            list1, list2 = lists[i], lists[i + 1]

            while list1 and list2:
                if list1.val <= list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2= list2.next
                node = node.next
            node.next = list1 or list2
            lists[i + 1] = head.next
        
        return lists[-1] if len(lists) > 0 else None