# time: O(n)
# memory: O(1)
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        answer = 0
        
        for i in range(1, len(arrays)):
            arr = arrays[i]
            answer = max(answer, arr[-1] - min_val, max_val - arr[0])
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        
        return answer
