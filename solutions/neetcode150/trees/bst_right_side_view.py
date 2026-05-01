from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # the right side view consists of the rightmost element at each level
        # do a level-order traversal, add the rightmost elements at each level to the result
        queue = deque([root])
        res = []

        while queue:
            right_most = None
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                if node:
                    right_most = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right_most:
                res.append(right_most.val)

        return res
