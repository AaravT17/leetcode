# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid(root, float('-inf'), float('inf'))

    def _is_valid(self, root: Optional[TreeNode], lower_bound: int, upper_bound: int) -> bool:
        if not root:
            return True

        return (
            lower_bound < root.val < upper_bound
            and self._is_valid(root.left, lower_bound, root.val)
            and self._is_valid(root.right, root.val, upper_bound)
        )
