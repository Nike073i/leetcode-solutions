# time: O(n)
# memory: O(2^k)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        combinations = set()
        
        for i in range(k, len(s) + 1):
            combinations.add(s[i - k:i])

        return len(combinations) == pow(2, k)
