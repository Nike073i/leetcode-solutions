# time: O(n)
# memory: O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 0
        count = 0

        for i in range(len(s)):
            curr += 1
            if i + 1 >= len(s) or s[i + 1] != s[i]:
                count += min(prev, curr)
                prev = curr
                curr = 0
                
        return count
