# time: O(n + m)
# memory: O(1)
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_distance = 0

        j = 0
        i = 0
        while i < len(nums1) and j < len(nums2):
            if j < i:
                j += 1
            elif nums2[j] >= nums1[i]:
                max_distance = max(max_distance, j - i)
                j += 1
            else:
                i += 1

        return max_distance
