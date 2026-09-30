class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # Approach 1: Find a cycle and remove any edge from it (here, remove the one that appears last in edges)
        # n = m = len(edges)  # a tree with n nodes has n-1 edges, here there is one additional edge => n = m

        # neighbours = [[] for i in range(n + 1)]
        # for a, b in edges:
        #     neighbours[a].append(b)
        #     neighbours[b].append(a)

        # parent = [-1] * (n + 1)
        # visited = [0] * (n + 1)
        # res = [[-1, -1]]

        # def dfs_visit(node: int):
        #     for nei in neighbours[node]:
        #         if nei == parent[node]:
        #             # nei is the node we came to the current node from, don't traverse the same edge again
        #             continue
        #         if visited[nei]:
        #             # cycle found
        #             cycle_edges = _trace_cycle(node, nei)
        #             for i in range(m - 1, -1, -1):
        #                 a, b = edges[i]
        #                 if (a, b) in cycle_edges:
        #                     res[0] = [a, b]
        #                     break
        #         else:
        #             parent[nei] = node
        #             visited[nei] = 1
        #             dfs_visit(nei)
        #         if res[0] != [-1, -1]:
        #             break

        # def _trace_cycle(from_node: int, to_node: int) -> set:
        #     cycle_edges = set()
        #     cycle_edges.add((min(from_node, to_node), max(from_node, to_node)))
        #     curr = from_node
        #     while curr != to_node:
        #         a, b = curr, parent[curr]
        #         curr = parent[curr]
        #         cycle_edges.add((min(a, b), max(a, b)))
        #     return cycle_edges

        # visited[1] = 1
        # dfs_visit(1)
        # return res[0]

        # Approach 2: Union Find
        n = len(edges)  # a tree with n nodes has n-1 edges, here there is one additional edge => n = len(edges)

        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)

        def _find_root(node: int) -> int:
            curr = node
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr

        def _union(node1: int, node2: int) -> bool:
            root1, root2 = _find_root(node1), _find_root(node2)

            if root1 == root2:
                return False

            if size[root1] > size[root2]:
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]
            return True

        for a, b in edges:
            if not _union(a, b):
                return [a, b]
