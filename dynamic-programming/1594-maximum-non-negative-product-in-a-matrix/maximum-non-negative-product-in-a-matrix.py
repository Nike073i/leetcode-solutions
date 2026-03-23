# time: O(n * m)
# memory: O(m)
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [ None ] * m

        def product(tp_1, tp_2, val):
            max_prod = max(tp_1[0], tp_2[0]) * val
            min_prod = min(tp_1[1], tp_2[1]) * val

            return (max_prod, min_prod) if val > 0 else (min_prod, max_prod)

        dp[0] = grid[0][0], grid[0][0]
        for j in range(1, m):
            dp[j] = product(dp[j - 1], dp[j - 1], grid[0][j])

        for i in range(1, n):
            dp[0] = product(dp[0], dp[0], grid[i][0])

            for j in range(1, m):
                dp[j] = product(dp[j - 1], dp[j], grid[i][j])

        max_product = max(dp[-1])
            
        return -1 if max_product < 0 else max_product % (10 ** 9 + 7)
