# time: O(n log n)
# memory: O(n)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        max_diff = 0

        for i in range(1, len(sorted_nums)):
            max_diff = max(max_diff, sorted_nums[i] - sorted_nums[i - 1])

        return max_diff
