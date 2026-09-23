# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest path in a tree is one of the following:
        #   - longest path in left subtree
        #   - longest path in right subtree
        #   - longest path through root i.e. lowest node in left subtree to lowest node in right subtree through root
        height, diameter = self._get_height_and_diameter(root)
        return diameter
    
    def _get_height_and_diameter(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if not root:
            return (-1, -1)
        
        left_height, left_diameter = self._get_height_and_diameter(root.left)
        right_height, right_diameter = self._get_height_and_diameter(root.right)

        return (1 + max(left_height, right_height), max(left_diameter, right_diameter, 2 + left_height + right_height))