# time: O(n * m)
# memory: O(n * m)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = [ [False] * cols for _ in range(rows) ]       

        def dfs(i, j):
            if not (0 <= i < rows and 0 <= j < cols):
                return
            
            if board[i][j] != 'O' or visited[i][j]:
                return

            visited[i][j] = True

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj)
            
        for i in range(rows):
            if (board[i][0] == 'O'):
                dfs(i, 0)
            if (board[i][cols - 1] == 'O'):
                dfs(i, cols - 1)

        for j in range(cols):
            if (board[0][j] == 'O'):
                dfs(0, j)
            if (board[rows - 1][j] == 'O'):
                dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    board[i][j] = 'X'
