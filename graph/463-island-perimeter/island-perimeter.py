# time: O(n * m)
# memory: O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def is_water(i, j):
            if not (0 <= i < n and 0 <= j < m):
                return True
            
            return grid[i][j] == 0

        directions = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

        def count_water_neighbors(i, j):
            return sum(is_water(i + di, j + dj) for di, dj in directions)

        perimeter = 0
        for i in range(n):
            for j in range(m):
                if not is_water(i, j):
                    perimeter += count_water_neighbors(i, j)
        
        return perimeter
