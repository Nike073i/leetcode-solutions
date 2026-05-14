# time: O(n)
# memory: O(1) # 101 max
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        flags = [ False ] * len(nums)
        n_count = 0

        for num in nums:
            if num > n: 
                return False
            elif num == n:
                if n_count < 2:
                    n_count += 1
                else: 
                    return False
            else:
                if flags[num]: 
                    return False
                flags[num] = True

        return True
