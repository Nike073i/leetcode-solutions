# time: O(n)
# memory: O(1)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        length = len(colors)
        for i in range(length):
            if colors[0] != colors[-i - 1] or colors[-1] != colors[i]:
                return length - i - 1

        return 0
