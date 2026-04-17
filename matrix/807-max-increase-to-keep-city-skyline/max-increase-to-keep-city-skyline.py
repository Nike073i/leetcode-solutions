# time: O(n * m)
# memory: O(n + m)
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_rows = [ 0 ] * n
        max_cols = [ 0 ] * m
        
        for i in range(n):
            for j in range(m):
                max_rows[i] = max(max_rows[i], grid[i][j])
                max_cols[j] = max(max_cols[j], grid[i][j])

        total = 0
        for i in range(n):
            for j in range(m):
                total += min(max_rows[i], max_cols[j]) - grid[i][j]

        return total
