# time: O(n)
# memory: O(1)
class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            count += (ord(s[i]) - ord('0')) ^ (i & 1)

        return min(count, len(s) - count)
