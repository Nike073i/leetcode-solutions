# time: O(1)
# memory: O(1)
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def is_interval_overlap(a, b):
            if b[0] < a[0]:
                a, b = b, a

            return a[1] > b[0]

        return is_interval_overlap(
            [rec1[0], rec1[2]], [rec2[0], rec2[2]]
        ) and is_interval_overlap([rec1[1], rec1[3]], [rec2[1], rec2[3]])
