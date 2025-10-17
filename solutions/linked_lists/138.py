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

        # Step 1: Create copies of each of the nodes in the original linked list
        # and store them in a hashmap (key = original node, value = copy)
        h = {}
        curr = head
        while curr:
            curr_copy = Node(x=curr.val)
            h[curr] = curr_copy
            curr = curr.next

        # Step 2: Create the new list i.e. make the connections between the
        # copies
        curr = head
        while curr:
            curr_copy = h[curr]
            curr_copy.next = h[curr.next] if curr.next else None
            curr_copy.random = h[curr.random] if curr.random else None
            curr = curr.next

        return h[head]
