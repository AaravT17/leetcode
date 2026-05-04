from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort
        # run DFS, once a course is visited completely, append to result, if at any point a cycle is detected, we
        # cannot take all courses so return []

        # construct adjacency list
        adj_list = {u: [] for u in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = [UNVISITED] * numCourses
        res = []

        def dfs(u: int) -> bool:
            # return True if we can finish this course, and False otherwise
            if status[u] == VISITED:
                return True
            if status[u] == VISITING:
                # we arrived back at this course while visiting it/seeing if we can finish it => cycle
                return False

            status[u] = VISITING

            for v in adj_list[u]:
                if not dfs(v):
                    return False

            # we could complete all courses required to take this course, so we can take this course as well
            status[u] = VISITED
            res.append(u)
            return True

        for u in range(numCourses):
            if not dfs(u):
                return []

        return res
        # Time: O(n + m), Space: O(n + m) where n = numCourses, m = len(prerequisites)
