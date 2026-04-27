# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Approach 1
        # Invert/mirror one subtree and check if it is the same as the other (after inversion/mirroring)
        # def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #     if not p and not q:
        #         return True

        #     if not p or not q:
        #         return False

        #     return (
        #         p.val == q.val
        #         and isSameTree(p.left, q.left)
        #         and isSameTree(p.right, q.right)
        #     )

        # def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        #     if not root:
        #         return None

        #     return TreeNode(root.val, invertTree(root.right), invertTree(root.left))

        # if not root:
        #     return True

        # if not root.left and not root.right:
        #     return True

        # if not root.left or not root.right:
        #     return False

        # return isSameTree(root.left, invertTree(root.right))

        # Approach 2
        def isMirror(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True

            if not p or not q:
                return False

            return (
                p.val == q.val
                and isMirror(p.left, q.right)
                and isMirror(p.right, q.left)
            )

        return not root or isMirror(root.left, root.right)
