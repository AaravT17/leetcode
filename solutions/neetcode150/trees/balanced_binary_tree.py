# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = [True]

        def _get_height(root: Optional[TreeNode]) -> int:
            if not root:
                return -1

            left_height = _get_height(root.left)

            if not is_balanced[0]:
                return 0

            right_height = _get_height(root.right)

            if not is_balanced[0]:
                return 0

            if abs(left_height - right_height) > 1:
                is_balanced[0] = False
            
            return 1 + max(left_height, right_height)
        
        _get_height(root)
        return is_balanced[0]