from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_map = {}  # maps original node -> copy

        def _create_copies(node: Optional['Node']):
            seen = set()
            q = deque([node])
            while q:
                curr = q.popleft()
                seen.add(curr)
                node_map[curr] = Node(val=curr.val)
                for curr in curr.neighbors:
                    if curr not in seen:
                        q.append(curr)

        def _add_neighbors():
            for orig in node_map:
                cpy = node_map[orig]
                for n in orig.neighbors:
                    cpy.neighbors.append(node_map[n])

        _create_copies(node)
        _add_neighbors()
        return node_map[node]
