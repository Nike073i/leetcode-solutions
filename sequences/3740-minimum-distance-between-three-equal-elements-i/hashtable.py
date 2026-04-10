# time: O(n)
# memory: O(n)
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        elements = { }

        for i, num in enumerate(nums):
            indexes = elements.get(num, [])
            indexes.append(i)
            elements[num] = indexes

        min_distance = math.inf
        for num, indexes in elements.items():
            if len(indexes) > 2:
                for i in range(len(indexes) - 2):
                    min_distance = min(
                        min_distance, 
                            abs(indexes[i] - indexes[i + 1]) +
                            abs(indexes[i + 1] - indexes[i + 2]) +
                            abs(indexes[i + 2] - indexes[i])
                        )

        if min_distance == math.inf:
            min_distance = -1
        
        return min_distance
