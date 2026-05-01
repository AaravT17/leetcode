from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest path is either longest path on the left, longest path on the right, or longest path through
        # the root, which is equal to 2 + height of left tree + height of right tree
        if not root:
            return 0

        return self.get_height_and_longest_path(root)[1]

    def get_height_and_longest_path(self, root: TreeNode) -> tuple[int, int]:
        # never called on an empty tree i.e. root is not None
        # returns (height, diameter) of tree rooted at root
        left_res = (
            self.get_height_and_longest_path(root.left) if root.left else (-1, -1)
        )
        right_res = (
            self.get_height_and_longest_path(root.right) if root.right else (-1, -1)
        )

        return (
            1 + max(left_res[0], right_res[0]),
            max(left_res[1], right_res[1], 2 + left_res[0] + right_res[0]),
        )
