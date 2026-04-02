# time: O(log_7(n))
# memory: O(log_7(n))
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        alphabet = "0123456"
        result = [ ]

        tmp = abs(num)

        while tmp > 0:
            result.append(alphabet[tmp % 7])
            tmp //= 7

        if num < 0:
            result.append("-")
        
        for i in range(len(result) // 2):
            result[i], result[-i - 1] = result[-i - 1], result[i]
        
        return "".join(result)
