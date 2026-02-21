# time: O(n)
# memory: O(1)
class Solution:
    def is_simple(self, x):
        return x in { 2, 3, 5, 7, 11, 13, 17, 19}

    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(1 for i in range(left, right + 1) if self.is_simple(i.bit_count()) )
