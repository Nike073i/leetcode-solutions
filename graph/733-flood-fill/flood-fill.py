# time: O(n * m)
# memory: O(n * m)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target_color = image[sr][sc]
        if target_color == color:
            return image

        directions = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

        def dfs(i, j):
            if not (0 <= i < len(image) and 0 <= j < len(image[0])):
                return

            if image[i][j] != target_color:
                return
            
            image[i][j] = color
            for di, dj in directions:
                dfs(i + di, j + dj)

        dfs(sr, sc)
            
        return image
