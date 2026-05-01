from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # Step 1: Create copies of each of the nodes in the original linked list and store them
        # in a hashmap (key = original node, value = copy)
        node_map = {}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Create the new list i.e. make the connections between the copies
        curr = head
        while curr:
            node = node_map[curr]
            node.next = node_map[curr.next] if curr.next is not None else None
            node.random = node_map[curr.random] if curr.random is not None else None
            curr = curr.next

        return node_map[head]
        # Time: O(n), Space: O(n)
