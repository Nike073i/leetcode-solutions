# time: O(n * m)
# memory: O(m)
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        prefixX = [ 0 ] * m
        prefixY = [ 0 ] * m

        count = 0

        for i in range(n):
            rX = 0
            rY = 0
            for j in range(m):
                if grid[i][j] == 'X':
                    prefixX[j] += 1
                elif grid[i][j] == 'Y':
                    prefixY[j] += 1

                rX += prefixX[j]
                rY += prefixY[j]

                if rX and rX == rY:
                    count += 1

        return count
                
