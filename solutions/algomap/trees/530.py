# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Approach 1
        # at any node, the minimum absolute difference is one of the following:
        #   - the minimum absolute difference in the left subtree
        #   - the minimum absolute difference in the right subtree
        #   - the absolute difference between the node's value and the maximum value in the left subtree
        #   - the absolute difference between the node's value and the minimum value in the right subtree
        def min_max_min_abs_diff(node: Optional[TreeNode]) -> tuple[int, int, int]:
            # Precondition: node is non-null
            left, right = None, None
            if node.left:
                left = min_max_min_abs_diff(node.left)
            if node.right:
                right = min_max_min_abs_diff(node.right)
            min_val = min(node.val, left[0] if left else node.val)
            max_val = max(node.val, right[1] if right else node.val)
            if left and right:
                min_abs_diff = min(
                    left[2], right[2], abs(node.val - left[1]), abs(node.val - right[0])
                )
            elif left:
                min_abs_diff = min(left[2], abs(node.val - left[1]))
            elif right:
                min_abs_diff = min(right[2], abs(node.val - right[0]))
            else:
                min_abs_diff = float('inf')

            return (min_val, max_val, min_abs_diff)

        return min_max_min_abs_diff(root)[2]

        # Approach 2
        # min_abs_diff = [float('inf')]
        # prev = [None]

        # def dfs(node: Optional[TreeNode]) -> None:
        #     if not node:
        #         return

        #     dfs(node.left)

        #     if prev[0] is not None:
        #         min_abs_diff[0] = min(min_abs_diff[0], node.val - prev[0])

        #     prev[0] = node.val

        #     dfs(node.right)

        # dfs(root)
        # return min_abs_diff[0]
