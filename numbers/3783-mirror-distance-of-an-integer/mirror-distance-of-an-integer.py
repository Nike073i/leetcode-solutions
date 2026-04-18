# time: O(log10n)
# memory: O(1)
class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        mirror = 0

        while n > 0:
            mirror *= 10
            mirror += n % 10
            n //= 10
        
        return abs(original - mirror)
