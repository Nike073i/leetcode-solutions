# time: O(nlogn)
# memory: O(n)

class Solution:
    def bit_count(self, n):
        count = 0
        while n > 0:
            count += (n & 1)
            n >>= 1

        return count

    def sortByBits(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)

        digits = { }
        
        for elem in sorted_arr:
            bits = self.bit_count(elem)
            coll = digits.get(bits, [])
            coll.append(elem)
            digits[bits] = coll
        
        result = []
        for i in range(14):
            coll = digits.get(i, [])
            result += coll

        return result
