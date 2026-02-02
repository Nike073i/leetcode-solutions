# time: O(n * m)
# memory: O(1)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def is_good(i, j):
            isUpFree = i == 0 or board[i - 1][j] == '.'
            isLeftFree = j == 0 or board[i][j - 1] == '.'
            return isUpFree and isLeftFree

        k = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if is_good(i, j) and board[i][j] == 'X':
                    k += 1

        return k
        
