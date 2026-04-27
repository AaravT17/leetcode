# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True

            if not p or not q:
                return False

            return (
                p.val == q.val
                and isSameTree(p.left, q.left)
                and isSameTree(p.right, q.right)
            )

        if not root:
            return False

        if root.val == subRoot.val and isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # n: size of the tree, h1: height of the tree, m: size of the subtree, h2: height of the subtree
        # Time: O(m * n), since we check at each of the n nodes (in the worst case) whether the tree rooted at
        #   that node is the same as the subtree (can be optimized to be O(m + n))
        # Space: O(h2 + h1), which is O(m + n) in the worst case (imbalanced/skewed tree), since the stack holds
        #   the call stack for recursive calls down one path of the tree at a time along with the call stacks for
        #   tree similarity check, which consists of recursive calls down one path of the subtree at a time
