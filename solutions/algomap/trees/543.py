# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # the diameter of a binary tree is the length of the longest path between any two nodes in the tree
        # at each node, there are 3 candidates for the longest path:
        #   - the longest path in the left subtree
        #   - the longest path in the right subtree
        #   - the path from the deepest node in the left subtree to the deepest node in the right subtree
        #     through the current node
        def height_longest_path(root: Optional[TreeNode]) -> tuple[int, int]:
            if not root:
                return (-1, -1)

            left = height_longest_path(root.left)
            right = height_longest_path(root.right)

            return (
                1 + max(left[0], right[0]),
                max(left[1], right[1], 2 + left[0] + right[0]),
            )

        return height_longest_path(root)[1]
