class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbours = {course: [] for course in range(numCourses)}
        for a, b in prerequisites:
            neighbours[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = [UNVISITED] * numCourses

        def dfs_visit(course: int) -> bool:
            status[course] = VISITING

            for n in neighbours[course]:
                if status[n] == VISITED:
                    continue
                if status[n] == VISITING:
                    return False
                if not dfs_visit(n):
                    return False

            status[course] = VISITED
            return True

        for course in range(numCourses):
            if status[course] == UNVISITED:
                if not dfs_visit(course):
                    return False

        return True
        # Time: O(n + m), Space: O(n + m), where n = numCourses, m = len(prerequisites)
