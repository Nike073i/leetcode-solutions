# time: O(n * m)
# memory: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        for i in range(n // 2):
            for j in range(m):
                matrix[i][j], matrix[-(i + 1)][j] = matrix[-(i + 1)][j], matrix[i][j]

        for i in range(n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
