# memory: O(n)
# time: O(m * n)
class Solution:
    def createArray(self, length: int, default = 0) -> List[int]:
        return [default] * length

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        
        prev = self.createArray(n, 1)
        curr = self.createArray(n)

        for i in range(1, m):
            curr[0] = 1
            for j in range(1, n):
                curr[j] = prev[j] + curr[j - 1]
            prev, curr = curr, prev

        return prev[-1]
