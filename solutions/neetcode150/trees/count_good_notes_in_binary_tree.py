# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # At each recursive call, track the greatest value seen on the path from the root to the current node.
        return self._good_nodes(root, float('-inf'))

    def _good_nodes(self, node: Optional[TreeNode], max_ancestor: int) -> int:
        if not node:
            return 0

        is_good = int(node.val >= max_ancestor)
        new_max_ancestor = max(max_ancestor, node.val)

        return is_good + self._good_nodes(node.left, new_max_ancestor) + self._good_nodes(node.right, new_max_ancestor)
