# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # preorder -> root, inorder -> elements that belong in left and right subtrees
        n = len(preorder)
        inorder_val_idx_map = {inorder[i]: i for i in range(n)}  # maps value -> index in inorder

        def _build_tree(root_idx: int, l: int, r: int) -> TreeNode | None:
            if l > r:
                # no nodes in this subtree
                return None

            # this tree is in [l, r] in inorder, and its root is at root_idx in preorder
            root_val = preorder[root_idx]
            root = TreeNode(val=root_val)
            root_idx_inorder = inorder_val_idx_map[root_val]
            # left subtree is in [l, root_idx_inorder - 1], right subtree is in [root_idx_inorder + 1, r] in inorder
            left_subtree_size = root_idx_inorder - l  # = (root_idx_inorder - 1) - l + 1
            root.left = _build_tree(root_idx + 1, l, root_idx_inorder - 1)
            root.right = _build_tree(root_idx + 1 + left_subtree_size, root_idx_inorder + 1, r)
            return root

        return _build_tree(0, 0, n - 1)
