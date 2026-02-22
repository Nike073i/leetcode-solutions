# time: O(logn)
# memory: O(logn)
class Solution:
    def binaryGap(self, n: int) -> int:
        l = 0
        r = 0
        distance = 0

        seq = bin(n)[2:]

        while r + 1 < len(seq):
            r += 1

            if seq[r] == "1":
                distance = max(distance, r - l)
                l = r

        return distance    
