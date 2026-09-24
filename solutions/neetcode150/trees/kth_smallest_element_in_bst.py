# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Do an in-order traversal and return the kth node seen.
        seen = [0]
        res = [-1]

        def dfs_visit(node: Optional[TreeNode]):
            if not node:
                return
            
            dfs_visit(node.left)
            if seen[0] == k:
                return
            
            seen[0] += 1
            if seen[0] == k:
                res[0] = node.val
                return
            
            dfs_visit(node.right)
        
        dfs_visit(root)
        return res[0]
