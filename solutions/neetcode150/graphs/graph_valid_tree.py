class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree: Connected, acyclic graph => starting from any node, reach all nodes + no cycles.
        # Shortcut: A tree with n nodes must have exactly n-1 edges. If num edges != n-1, the graph cannot
        # be a tree (either unconnected or has a cycle). So, check connected + num edges == n-1.
        neighbours = {i: [] for i in range(n)}
        for i, j in edges:
            neighbours[i].append(j)
            neighbours[j].append(i)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = [UNVISITED] * n

        def dfs_visit(curr: int, coming_from: int) -> bool:
            status[curr] = VISITING

            for nei in neighbours[curr]:
                if nei == coming_from or status[nei] == VISITED:
                    continue
                if status[nei] == VISITING:
                    return False
                if not dfs_visit(nei, curr):
                    return False

            status[curr] = VISITED
            return True

        return dfs_visit(0, -1) and all(s == VISITED for s in status)
