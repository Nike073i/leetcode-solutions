# time: O(n * m * 4^l), где l - длина слова
# memory: O(1 + recursive stack) ~= O(l), где l - длина слова
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        directions = [ (0, 1), (-1, 0), (0, -1), (1, 0) ]

        def dfs(i, j, k):
            if k >= len(word): return True
            if not (0 <= i < n and 0 <= j < m): return False
            if board[i][j] != word[k]: return False

            letter = board[i][j]
            board[i][j] = ''

            for di, dj in directions:
                if dfs(i + di, j + dj, k + 1):
                    return True
            
            board[i][j] = letter
            
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
                  
        return False
