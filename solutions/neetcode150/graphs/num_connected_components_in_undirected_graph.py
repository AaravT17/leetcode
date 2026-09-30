class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Approach 1: DFS
        neighbours = {i: [] for i in range(n)}
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()

        def dfs_visit(i: int):
            for nei in neighbours[i]:
                if nei not in visited:
                    visited.add(nei)
                    dfs_visit(nei)

        num_components = 0
        for i in range(n):
            if i not in visited:
                num_components += 1
                visited.add(i)
                dfs_visit(i)

        return num_components

        # Approach 2: Union Find
        # parent = [i for i in range(n)]
        # size = [1] * n

        # def _find_root(node):
        #     curr = node
        #     while curr != parent[curr]:
        #         parent[curr] = parent[parent[curr]]  # path compression
        #         curr = parent[curr]
        #     return curr

        # def _union(node1, node2) -> bool:
        #     root1, root2 = _find_root(node1), _find_root(node2)

        #     if root1 == root2:
        #         return False

        #     if size[root1] > size[root2]:
        #         parent[root2] = root1
        #         size[root1] += size[root2]
        #     else:
        #         parent[root1] = root2
        #         size[root2] += size[root1]
        #     return True

        # num_components = n
        # for a, b in edges:
        #     num_components -= int(_union(a, b))

        # return num_components
