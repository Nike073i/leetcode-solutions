# time: O(n * m)
# memory: O(n * m)
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])

        def average_pooling(i, j):
            total, count = 0, 0

            top = max(0, i - 1)
            bottom = min(rows, i + 2)
            left = max(0, j - 1)
            right = min(cols, j + 2)

            for row in range(top, bottom):
                for col in range(left, right):
                    total += img[row][col]
                    count += 1

            return total // count
        
        smoothed = [ [ average_pooling(i, j) for j in range(cols) ] for i in range(rows) ]
        
        return smoothed
