from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [None]
        seen = [0]

        def dfs_visit(node: Optional[TreeNode]):
            if not node:
                return

            dfs_visit(node.left)
            if res[0] is not None:
                return

            seen[0] += 1
            if seen[0] == k:
                res[0] = node.val
                return

            dfs_visit(node.right)

        dfs_visit(root)
        return res[0]
