# time: O(n), где n - длина строки s
# memory: O(1)
class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        count = 0
        while n > 1:
            if (n & 1) == 1:
                n += 1
            else:
                n >>= 1
            count += 1

        return count
