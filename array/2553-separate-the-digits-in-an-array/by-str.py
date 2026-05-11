class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(ch) for num in nums for ch in str(num)]
