# time: O(n^2)
# memory: O(n^2)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        DEFAULT_VALUE = 0

        matrix = [ [DEFAULT_VALUE] * n for _ in range(n) ]

        directions = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

        direction_idx = 0
        position = (0, 0)

        def move(position, direction_idx):
            next_i = position[0] + directions[direction_idx][0]
            next_j = position[1] + directions[direction_idx][1]
            return (next_i, next_j)

        def has_next(position, direction_idx):
            next_i = position[0] + directions[direction_idx][0]
            next_j = position[1] + directions[direction_idx][1]
            
            if not 0 <= next_i < n or not 0 <= next_j < n:
                return False
            
            return matrix[next_i][next_j] == DEFAULT_VALUE

        def change_direction(direction_idx):
            return (direction_idx + 1) % len(directions)

        for i in range(1, pow(n, 2) + 1):
            matrix[position[0]][position[1]] = i

            if not has_next(position, direction_idx):
                direction_idx = change_direction(direction_idx)
            
            position = move(position, direction_idx)

        return matrix
