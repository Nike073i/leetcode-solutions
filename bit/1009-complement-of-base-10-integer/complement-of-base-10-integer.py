# time: O(logn)
# memory: O(1)
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1

        mask = 0b0

        while mask < n:
            mask = (mask << 1) + 1

        # or mask = (1 << n.bit_length()) - 1

        return n ^ mask
