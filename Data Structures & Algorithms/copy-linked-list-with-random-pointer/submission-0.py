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
        if not head:
            return None

        # Map original nodes → copied nodes
        old_to_new = {}

        # 1st pass: copy nodes (values only)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 2nd pass: assign next + random pointers
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next, None)
            copy.random = old_to_new.get(curr.random, None)
            curr = curr.next

        # Return the deep copied head
        return old_to_new[head]

        




        
        