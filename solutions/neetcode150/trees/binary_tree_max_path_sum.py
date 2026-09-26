# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_in_tree, max_through_root = self._max_path_sum(root)
        return max_in_tree

    def _max_path_sum(self, root: TreeNode | None) -> tuple[int, int]:
        """
        Return the maximum path sum in the subtree rooted at root, and the maximum path sum in the subtree
        that includes/passes through root.
        """
        if not root:
            return float('-inf'), float('-inf')

        left_max, left_max_through_root = self._max_path_sum(root.left)
        right_max, right_max_through_root = self._max_path_sum(root.right)
        max_through_root = root.val + max(left_max_through_root, right_max_through_root, 0)
        # max_through_root: The maximum additional path sum you can get if you choose to continue the path
        # from the parent down through this node. Note that we can only choose to connect from the root to
        # at most one of its left and right subtrees (since a node can only appear once on the path).
        max_in_tree = max(
            left_max, right_max, root.val + max(left_max_through_root, 0) + max(right_max_through_root, 0)
        )
        # max_in_tree: The maximum path sum in the subtree rooted at this node. Note that, to compute this,
        # we can choose to connect to both of the node's subtrees if we wish (since we are computing this as
        # though this node is the root of the tree and it has no parent).
        return max_in_tree, max_through_root
