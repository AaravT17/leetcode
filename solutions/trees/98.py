# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Approach 1
        def is_valid_bst_recursive(
            node: Optional[TreeNode], min_val: int, max_val: int
        ) -> bool:
            if not node:
                return True

            return (
                (node.val > min_val and node.val < max_val)
                and is_valid_bst_recursive(node.left, min_val, node.val)
                and is_valid_bst_recursive(node.right, node.val, max_val)
            )

        return is_valid_bst_recursive(root, float('-inf'), float('inf'))

        # Approach 2
        # valid = [True]
        # prev = [None]

        # def dfs(node: Optional[TreeNode]) -> None:
        #     if not node:
        #         return

        #     dfs(node.left)

        #     if not valid[0]:
        #         return

        #     if prev[0] is not None and prev[0] >= node.val:
        #         valid[0] = False
        #         return

        #     prev[0] = node.val

        #     dfs(node.right)

        # dfs(root)
        # return valid[0]
