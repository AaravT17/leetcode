# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach 1
        def kth_smallest_recursive(
            root: Optional[TreeNode], k: int
        ) -> tuple[bool, int]:
            if not root:
                return (False, 0)

            left = kth_smallest_recursive(root.left, k)
            if left[0]:
                return (True, left[1])
            elif (
                left[1] == k - 1
            ):  # there are exactly k - 1 nodes in the left subtree, so the root is the kth smallest element
                return (True, root.val)

            right = kth_smallest_recursive(
                root.right, k - (left[1] + 1)
            )  # checked and skipped over the root + all elements in the left subtree
            if right[0]:
                return (True, right[1])
            return (
                False,
                left[1] + 1 + right[1],
            )  # return the number of elements checked and skipped over to inform the calling function

        return kth_smallest_recursive(root, k)[1]

        # Approach 2
        # count = [k]
        # res = [-1]

        # def dfs(node: Optional[TreeNode]) -> None:
        #     if not node:
        #         return

        #     dfs(node.left)

        #     if count[0] == 1:
        #         res[0] = node.val

        #     count[0] -= 1
        #     if count[0] > 0:
        #         dfs(node.right)

        # dfs(root)
        # return res[0]
