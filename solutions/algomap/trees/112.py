# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        new_target = targetSum - root.val
        if not root.left and not root.right:
            return new_target == 0

        return self.hasPathSum(root.left, new_target) or self.hasPathSum(
            root.right, new_target
        )
