# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The lowest common ancestor of p and q is the node at which we split up when searching for them i.e.
        # for one, we would have to go left, and for the other, we would have to go right. If one is an ancestor
        # of the other, then it is the lowest common ancestor.
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                # either we split our search at this node, or this node is p or q
                return curr

        return None
