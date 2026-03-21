# time: O(k^2)
# memory: O(1)
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        for i in range(k // 2):
            upper_row = grid[x+i]
            lower_row = grid[x + k - i - 1]

            for j in range(k):
                upper_row[y + j], lower_row[y + j]  = lower_row[y + j], upper_row[y + j]

        return grid
