from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Approach 1
        if not root:
            return []

        levels = []
        curr_level, curr_depth = [], 0
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            # any node popped from the queue is guaranteed to be non-null
            if depth != curr_depth:
                levels.append(curr_level)
                curr_level, curr_depth = [], depth
            curr_level.append(node.val)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        if curr_level:
            levels.append(curr_level)

        return levels

        # Approach 2
        # if not root:
        #     return []

        # levels = []

        # queue = deque([root])
        # while queue:
        #     curr_level = []
        #     n = len(queue)
        #     for i in range(n):
        #         node = queue.popleft()
        #         curr_level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     levels.append(curr_level)

        # return levels
