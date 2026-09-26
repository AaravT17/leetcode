# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # construct a str repr -> preorder repr of the tree (with null values to indicate missing nodes)
        preorder = []

        def dfs_visit(node: Optional[TreeNode]):
            if not node:
                preorder.append('N')
                return

            preorder.append(str(node.val))
            dfs_visit(node.left)
            dfs_visit(node.right)

        dfs_visit(root)
        while preorder and preorder[-1] == 'N':
            preorder.pop()
        return ','.join(preorder)  # if preorder == [], this returns ''

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(',')
        preorder = []
        for node in nodes:
            if node == 'N':
                preorder.append(None)
            else:
                preorder.append(int(node))

        n = len(preorder)
        i = [0]

        def _build_tree() -> Optional[TreeNode]:
            if i[0] >= n:
                return None
            # root is at preorder[i[0]]
            root_val = preorder[i[0]]
            i[0] += 1
            if root_val is None:
                return None
            root = TreeNode(val=root_val)
            root.left = _build_tree()
            root.right = _build_tree()
            return root

        return _build_tree()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
