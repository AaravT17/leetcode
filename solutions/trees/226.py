# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Modify in-place
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

        # Create a new tree
        # if not root:
        #     return None

        # return TreeNode(
        #     root.val, self.invertTree(root.right), self.invertTree(root.left)
        # )
