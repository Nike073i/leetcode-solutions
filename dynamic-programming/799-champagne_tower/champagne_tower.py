# time: O(n^2), где n - кол-во рядов
# memory: O(n^2)
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * (row + 1) for row in range(query_row + 1)]
        tower[0][0] = poured
        
        for row in range(query_row):
            for col in range(row + 1):
                if tower[row][col] > 1:
                    overflow = (tower[row][col] - 1) / 2.0
                    tower[row + 1][col] += overflow
                    tower[row + 1][col + 1] += overflow
        
        return min(1.0, tower[query_row][query_glass])
