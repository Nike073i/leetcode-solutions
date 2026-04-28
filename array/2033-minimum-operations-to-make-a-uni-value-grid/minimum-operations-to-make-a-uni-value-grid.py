# time: O(L log L), где L - это n * m
# memory: O(L)
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n, m = len(grid), len(grid[0])
        length = n * m
        sorted_vector = sorted([ col for row in grid for col in row ])

        median = sorted_vector[length // 2]
        count = 0
        for i in range(length):
            diff = abs(sorted_vector[i] - median)
            if diff % x != 0:
                return -1
            count += diff // x
        
        return count
