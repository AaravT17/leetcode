class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)
        left_wall, right_wall, top_wall, bottom_wall = 0, n - 1, 0, m - 1

        res = []
        x, y = 0, 0
        direction = RIGHT
        while len(res) < m * n:
            res.append(matrix[x][y])
            if direction == RIGHT and y == right_wall:
                direction = DOWN
                top_wall += 1
            elif direction == DOWN and x == bottom_wall:
                direction = LEFT
                right_wall -= 1
            elif direction == LEFT and y == left_wall:
                direction = UP
                bottom_wall -= 1
            elif direction == UP and x == top_wall:
                direction = RIGHT
                left_wall += 1
            dx, dy = direction
            x, y = x + dx, y + dy

        return res
