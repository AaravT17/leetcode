"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        node_map = {} # maps original node -> copy
        curr = head
        while curr:
            node_map[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head
        while curr:
            cpy = node_map[curr]
            cpy.next = node_map[curr.next] if curr.next else None
            cpy.random = node_map[curr.random] if curr.random else None
            curr = curr.next
        
        return node_map[head]
        # Time: O(n), Space: O(n)
