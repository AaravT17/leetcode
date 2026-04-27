# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # A balanced binary tree is one where no two leaf nodes differ in depth by more than 1
        # Approach 1
        # def height(root: Optional[TreeNode]) -> int:
        #     if not root:
        #         return -1

        #     return 1 + max(height(root.left), height(root.right))

        # if not root:
        #     return True

        # return (
        #     abs(height(root.left) - height(root.right)) <= 1
        #     and self.isBalanced(root.left)
        #     and self.isBalanced(root.right)
        # )

        # Approach 2
        # Optimize by avoiding repeated traversals down the tree by checking balance at each level as we recursively
        # calculate the height of the tree + early return
        balanced = [True]

        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return -1

            left = height(root.left)
            if not balanced[0]:
                return 0

            right = height(root.right)
            if not balanced[0]:
                return 0

            if abs(right - left) > 1:
                balanced[0] = False

            return 1 + max(left, right)

        height(root)
        return balanced[0]
