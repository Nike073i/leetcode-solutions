# time: O(n * m)
# memory: O(n * m)
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(prev_i, prev_j, i, j, value):
            if not (0 <= i < n and 0 <= j < m) or grid[i][j] != value:
                return False

            if (i, j) in visited:
                return True

            visited.add((i, j))

            for di, dj in directions:
                next_i = i + di
                next_j = j + dj
                if (next_i, next_j) != (prev_i, prev_j) and dfs(
                    i, j, next_i, next_j, value
                ):
                    return True

            return False

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and dfs(-1, -1, i, j, grid[i][j]):
                    return True

        return False
