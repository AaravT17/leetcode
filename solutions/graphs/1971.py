from typing import List
from collections import deque


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # Approach 1: Recursive DFS
        if source == destination:
            return True

        adj_list = {}
        for u, v in edges:
            if u in adj_list:
                adj_list[u].append(v)
            else:
                adj_list[u] = [v]

            if v in adj_list:
                adj_list[v].append(u)
            else:
                adj_list[v] = [u]

        seen = {source}

        def dfs_visit(curr: int) -> bool:
            if curr == destination:
                return True

            for neighbour in adj_list[curr]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs_visit(neighbour):
                        return True

            return False

        return dfs_visit(source)

        # Approach 2: Iterative DFS
        # if source == destination:
        #     return True

        # adj_list = {}
        # for u, v in edges:
        #     if u in adj_list:
        #         adj_list[u].append(v)
        #     else:
        #         adj_list[u] = [v]

        #     if v in adj_list:
        #         adj_list[v].append(u)
        #     else:
        #         adj_list[v] = [u]

        # seen = {source}
        # stack = [source]

        # while stack:
        #     curr = stack.pop()
        #     if curr == destination:
        #         return True

        #     for neighbour in adj_list[curr]:
        #         if neighbour not in seen:
        #             seen.add(neighbour)
        #             stack.append(neighbour)

        # return False

        # Approach 3: BFS
        # if source == destination:
        #     return True

        # adj_list = {}
        # for u, v in edges:
        #     if u in adj_list:
        #         adj_list[u].append(v)
        #     else:
        #         adj_list[u] = [v]

        #     if v in adj_list:
        #         adj_list[v].append(u)
        #     else:
        #         adj_list[v] = [u]

        # seen = {source}
        # queue = deque([source])

        # while queue:
        #     curr = queue.popleft()
        #     if curr == destination:
        #         return True

        #     for neighbour in adj_list[curr]:
        #         if neighbour not in seen:
        #             seen.add(neighbour)
        #             queue.append(neighbour)

        # return False
