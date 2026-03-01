# time: O(2^n * n)
# memory: O(2^n * n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = [ [] ]

        for elem in nums:
            for i in range(len(combinations)):
                combinations.append(combinations[i] + [elem])

        return combinations
