def sign(a):
    return (a > 0) - (a < 0)

# time: O(n)
# memory: O(1)
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        K = 3 # Trionic
        length = len(nums)

        def until_mono(index, direction):
            while index < length and sign(nums[index] - nums[index - 1]) == direction:
                index += 1    
            return index

        def get_direction(index):
            return 1 if index % 2 == 0 else -1

        index = 1
        for i in range(K):
            next_index = until_mono(index, get_direction(i))

            if next_index == index:
                return False

            index = next_index

        return index == length
