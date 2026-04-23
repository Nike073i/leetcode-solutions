# time: O(n)
# memory: O(n)
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        digits = { }

        for i in range(len(nums)):
            indexes, total = digits.get(nums[i], ([], 0))
            indexes.append(i)
            total += i
            digits[nums[i]] = (indexes, total)

        result = [ 0 ] * len(nums)

        for indexes, total in digits.values():
            len_indexes = len(indexes)

            if len_indexes == 1:
                continue
            
            result[indexes[0]] = total - indexes[0] * len_indexes

            for i in range(1, len_indexes):
                delta = indexes[i] - indexes[i - 1]
                rest_of_elements = len_indexes - i
                closer_to = rest_of_elements * delta
                further_on = i * delta
                result[indexes[i]] = result[indexes[i - 1]] - closer_to + further_on
        
        return result
