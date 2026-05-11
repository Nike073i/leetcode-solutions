# time: O(n), где n - суммарное кол-во цифр во всех числах
# memory: O(n)
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            digits = []
            while num > 0:
                digits.append(num % 10)
                num //= 10
            result.extend(reversed(digits))
        return result
