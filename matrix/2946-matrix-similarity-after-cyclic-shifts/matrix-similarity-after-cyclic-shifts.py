# time: O(n * m)
# memory: O(1)
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])
        k %= cols

        if k == 0:
            return True

        def check_shift(row, get_shifted):
            for i in range(cols):
                if row[i] != get_shifted(row, i):
                    return False

            return True

        shifts = [
            lambda row, i: row[(k + i) % cols],
            lambda row, i: row[-k + i]
        ]
            
        for i in range(rows):
            if not check_shift(mat[i], shifts[i % 2]):
                return False
        
        return True
