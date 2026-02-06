# time: O(nlogn)
# memory: O(1)
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        length = len(nums)

        sorted_nums = sorted(nums)

        l, r  = 0, 0
        min_removed = length - 1

        while r < length - 1 and l < length:
            if sorted_nums[r + 1] <= sorted_nums[l] * k:
                r += 1
                min_removed = min(min_removed, l + length - r - 1)
            else:
                l += 1
                r = max(l, r)

        return min_removed
        
