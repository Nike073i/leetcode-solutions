# time: O(n * m)
# memory: O(m)
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        columnSums = [0] * m
        count = 0

        for i in range(n):
            rowSum = 0
            for j in range(m):
                columnSums[j] += grid[i][j]
                rowSum += columnSums[j]
                if rowSum <= k:
                    count += 1

        return count
