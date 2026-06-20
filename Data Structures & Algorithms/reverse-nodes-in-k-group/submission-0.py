# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        def get_kth_node(node: ListNode, k: int) -> None | ListNode:
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        while True:
            kth_node = get_kth_node(prevGroup, k)
            if kth_node is None:
                break
            next_group = kth_node.next
            prev, curr = kth_node.next, prevGroup.next

            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevGroup.next
            prevGroup.next = kth_node
            prevGroup = temp

        return dummy.next
