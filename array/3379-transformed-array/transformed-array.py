# time: O(n)
# memory: O(n)
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        
        for i in range(length):
            j = (i + nums[i]) % length
            result[i] = nums[j]

        return result
