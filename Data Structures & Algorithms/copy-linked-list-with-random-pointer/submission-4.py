"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #solution without collections.defaultdict
        
        old_to_copy: dict = {None: None}

        curr = head
        while curr:
            node = old_to_copy.get(curr, Node(0))
            old_to_copy[curr] = node
            node.val = curr.val

            next_node = old_to_copy.get(curr.next, Node(0))
            old_to_copy[curr.next] = next_node
            node.next = next_node

            random_node = old_to_copy.get(curr.random, Node(0))
            old_to_copy[curr.random] = random_node
            node.random = random_node

            curr = curr.next
        
        return old_to_copy[head]
