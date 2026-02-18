# time: O(logn)
# memory: O(1)
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n & 1
        n >>= 1

        while n > 0:
            if n & 1 == last:
                return False
            last = n & 1
            n >>= 1
        
        return True
