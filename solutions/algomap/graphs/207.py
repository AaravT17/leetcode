from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj_list[a].append(b)

        WHITE, GREY, BLACK = 0, 1, 2
        # WHITE: Yet to be seen/visited
        # GREY: Seen, and currently exploring connected nodes
        # BLACK: Explored, and explored all connected nodes as well

        status = [WHITE] * numCourses

        def dfs_visit(course: int) -> bool:
            status[course] = GREY
            for neighbour in adj_list[course]:
                if status[neighbour] == GREY:  # cycle detected
                    return False
                elif status[neighbour] == WHITE:
                    if not dfs_visit(neighbour):
                        return False

            status[course] = BLACK
            return True

        for course in range(numCourses):
            if status[course] == WHITE:
                if not dfs_visit(course):
                    return False

        return True
