from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect if a cycle exists, if one does, it is not possible to finish all courses
        # construct adjacency list
        adj_list = {u: [] for u in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = [UNVISITED] * numCourses

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
            return True

        for u in range(numCourses):
            if not dfs(u):
                return False

        return True
        # Time: O(n + m), Space: O(n + m) where n = numCourses, m = len(prerequisites)
