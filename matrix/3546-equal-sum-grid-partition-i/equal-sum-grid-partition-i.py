# time: O(n * m)
# memory: O(n + m)
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        rowSum = [ 0 ] * n
        colSum = [ 0 ] * m
        total = 0

        for i in range(n):
            for j in range(m):
                rowSum[i] += grid[i][j]
                colSum[j] += grid[i][j]
                total += grid[i][j]

        if total % 2 != 0:
            return False

        target = total // 2
        acc = 0
        for i in range(n):
            acc += rowSum[i]
            if acc == target:
                return True

        acc = 0
        for j in range(m):
            acc += colSum[j]
            if acc == target:
                return True

        return False
        
