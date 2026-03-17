# time: O(n!)
# memory: O(n!)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        permutations = []
        stack = []

        def backtracking(curr):
            if len(stack) == len(nums):
                permutations.append(stack.copy())
                return

            prev = -11
            for i in range(len(sorted_nums)):
                if i == curr or sorted_nums[i] == prev:
                    continue

                prev = sorted_nums[i]
                stack.append(prev)
                backtracking(i)
                stack.pop()
            
        backtracking(-1)
        return permutations
            
