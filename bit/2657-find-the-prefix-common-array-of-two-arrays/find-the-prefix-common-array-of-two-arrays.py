# time: O(n)
# memory: O(n)
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = b = 0
        result = []

        for i in range(len(A)):
            a |= ( 1 << A[i])
            b |= ( 1 << B[i])
            c = a & b
            result.append(c.bit_count())
        
        return result
