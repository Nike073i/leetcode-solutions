# time: O(log n)
# memory: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        
        def is_good(ind):
            return nums[ind] >= nums[0]

        l = 0
        r = len(nums) - 1
        while r - l > 1:
            m = (r - l) // 2 + l
            if is_good(m):
                l = m
            else:
                r = m
        
        return nums[r]
